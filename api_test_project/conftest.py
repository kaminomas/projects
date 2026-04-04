import pytest
import yaml
from utils.api_client import Client


@pytest.fixture(scope="session")
def config_data():
    with open("config/config.yaml", "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

@pytest.fixture
def api(config_data):
    c = Client(config_data["base_url"])
    c.login(config_data["username"], config_data["password"])
    return c