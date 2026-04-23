from __future__ import annotations

import hashlib
from abc import ABC, abstractmethod
from typing import Any

import requests


class CredentialEncryptor(ABC):
    """Abstract password encryption algorithm; swap implementations per platform."""

    @abstractmethod
    def encrypt(self, raw_value: str) -> str:
        raise NotImplementedError


class PlainTextEncryptor(CredentialEncryptor):
    def encrypt(self, raw_value: str) -> str:
        return raw_value


class Md5Encryptor(CredentialEncryptor):
    def encrypt(self, raw_value: str) -> str:
        return hashlib.md5(raw_value.encode("utf-8")).hexdigest()


class Sha256Encryptor(CredentialEncryptor):
    def encrypt(self, raw_value: str) -> str:
        return hashlib.sha256(raw_value.encode("utf-8")).hexdigest()


class BaseAuthStrategy(ABC):
    """Abstract API auth strategy: unified entry point for login and request signing."""

    auth_path = "/auth"

    def __init__(self, encryptor: CredentialEncryptor | None = None):
        self.encryptor = encryptor or PlainTextEncryptor()
        self.auth_context: dict[str, Any] = {}

    def authenticate(
        self,
        base_url: str,
        username: str,
        password: str,
        session: requests.Session | None = None,
    ) -> dict[str, Any]:
        http_client = session or requests.Session()
        payload = self.build_auth_payload(username, password)
        response = http_client.post(f"{base_url}{self.auth_path}", json=payload)
        response.raise_for_status()
        self.auth_context = self.extract_auth_context(response)
        return self.auth_context

    def prepare_request_kwargs(
        self,
        method: str,
        path: str,
        **kwargs: Any,
    ) -> dict[str, Any]:
        request_kwargs = dict(kwargs)
        headers = dict(request_kwargs.pop("headers", {}) or {})
        cookies = dict(request_kwargs.pop("cookies", {}) or {})

        headers.update(self.build_auth_headers(method=method, path=path, request_kwargs=request_kwargs))
        cookies.update(self.build_auth_cookies())

        if headers:
            request_kwargs["headers"] = headers
        if cookies:
            request_kwargs["cookies"] = cookies
        return request_kwargs

    def encrypt_password(self, raw_password: str) -> str:
        return self.encryptor.encrypt(raw_password)

    @abstractmethod
    def build_auth_payload(self, username: str, password: str) -> dict[str, Any]:
        raise NotImplementedError

    @abstractmethod
    def extract_auth_context(self, response: requests.Response) -> dict[str, Any]:
        raise NotImplementedError

    def build_auth_headers(
        self,
        method: str,
        path: str,
        request_kwargs: dict[str, Any],
    ) -> dict[str, str]:
        return {}

    def build_auth_cookies(self) -> dict[str, str]:
        return {}


class CookieTokenAuth(BaseAuthStrategy):
    """Exchange credentials for a token at login, then forward it via Cookie on later requests."""

    def build_auth_payload(self, username: str, password: str) -> dict[str, Any]:
        return {
            "username": username,
            "password": self.encrypt_password(password),
        }

    def extract_auth_context(self, response: requests.Response) -> dict[str, Any]:
        return {"token": response.json()["token"]}

    def build_auth_cookies(self) -> dict[str, str]:
        token = self.auth_context.get("token")
        if not token:
            return {}
        return {"token": token}


class BearerTokenAuth(BaseAuthStrategy):
    """Exchange credentials for a token at login, then forward it via Authorization: Bearer header."""

    def build_auth_payload(self, username: str, password: str) -> dict[str, Any]:
        return {
            "username": username,
            "password": self.encrypt_password(password),
        }

    def extract_auth_context(self, response: requests.Response) -> dict[str, Any]:
        return {"token": response.json()["token"]}

    def build_auth_headers(
        self,
        method: str,
        path: str,
        request_kwargs: dict[str, Any],
    ) -> dict[str, str]:
        token = self.auth_context.get("token")
        if not token:
            return {}
        return {"Authorization": f"Bearer {token}"}


def build_encryptor(encrypt_type: str = "plain") -> CredentialEncryptor:
    encryptor_mapping = {
        "plain": PlainTextEncryptor,
        "md5": Md5Encryptor,
        "sha256": Sha256Encryptor,
    }
    try:
        return encryptor_mapping[encrypt_type.lower()]()
    except KeyError as exc:
        raise ValueError(f"Unsupported encrypt type: {encrypt_type}") from exc


def build_auth_strategy(
    auth_type: str = "cookie_token",
    encrypt_type: str = "plain",
) -> BaseAuthStrategy:
    strategy_mapping = {
        "cookie_token": CookieTokenAuth,
        "bearer_token": BearerTokenAuth,
    }
    try:
        return strategy_mapping[auth_type.lower()](encryptor=build_encryptor(encrypt_type))
    except KeyError as exc:
        raise ValueError(f"Unsupported auth type: {auth_type}") from exc
