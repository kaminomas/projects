import pytest
import yaml
from selenium import webdriver

from utils.driver_factory import create_remote_driver


@pytest.fixture(scope="session")
def config_data():
    with open("config/config.yaml", "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


@pytest.fixture
def driver():
    d = webdriver.Remote(
        command_executor="http://localhost:4444/wd/hub",
        options=webdriver.ChromeOptions()
    )
    yield d
    d.quit()
