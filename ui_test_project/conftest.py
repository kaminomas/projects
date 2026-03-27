import pytest
import yaml

from utils.driver_factory import create_remote_driver


@pytest.fixture(scope="session")
def config_data():
    with open("config/config.yaml", "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


@pytest.fixture
def driver(config_data):
    browser = create_remote_driver(config_data["selenium_hub"])
    yield browser
    browser.quit()