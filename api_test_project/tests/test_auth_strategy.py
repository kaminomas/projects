from utils.auth import (
    BearerTokenAuth,
    CookieTokenAuth,
    Md5Encryptor,
    PlainTextEncryptor,
    Sha256Encryptor,
    build_auth_strategy,
)


def test_md5_encryptor():
    encryptor = Md5Encryptor()
    assert encryptor.encrypt("password123") == "482c811da5d5b4bc6d497ffa98491e38"


def test_sha256_encryptor():
    encryptor = Sha256Encryptor()
    assert encryptor.encrypt("password123") == "ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f"


def test_cookie_token_auth_uses_encryptor_for_login_payload():
    auth = CookieTokenAuth(encryptor=PlainTextEncryptor())
    assert auth.build_auth_payload("admin", "password123") == {
        "username": "admin",
        "password": "password123",
    }


def test_cookie_token_auth_injects_token_cookie():
    auth = CookieTokenAuth()
    auth.auth_context = {"token": "mock-token"}

    request_kwargs = auth.prepare_request_kwargs("PUT", "/booking/1", json={"firstname": "Tom"})

    assert request_kwargs["cookies"] == {"token": "mock-token"}
    assert request_kwargs["json"] == {"firstname": "Tom"}


def test_bearer_token_auth_injects_authorization_header():
    auth = BearerTokenAuth()
    auth.auth_context = {"token": "mock-token"}

    request_kwargs = auth.prepare_request_kwargs("GET", "/orders")

    assert request_kwargs["headers"] == {"Authorization": "Bearer mock-token"}


def test_build_cookie_auth_strategy():
    auth = build_auth_strategy(auth_type="cookie_token", encrypt_type="sha256")

    assert isinstance(auth, CookieTokenAuth)
    assert isinstance(auth.encryptor, Sha256Encryptor)


def test_build_bearer_auth_strategy():
    auth = build_auth_strategy(auth_type="bearer_token", encrypt_type="md5")

    assert isinstance(auth, BearerTokenAuth)
    assert isinstance(auth.encryptor, Md5Encryptor)
