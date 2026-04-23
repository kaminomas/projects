import pytest
import yaml
from utils.api_client import Client
from utils.auth import build_auth_strategy


@pytest.fixture(scope="session")
def config_data():
    with open("config/config.yaml", "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

@pytest.fixture
def api(config_data):
    auth_strategy = build_auth_strategy(
        auth_type=config_data.get("auth_type", "cookie_token"),
        encrypt_type=config_data.get("password_encrypt_type", "plain"),
    )
    c = Client(config_data["base_url"], auth_strategy=auth_strategy)
    c.login(config_data["username"], config_data["password"])
    return c
