import pytest
import yaml

@pytest.fixture(scope="session")
def config_data():
    with open("config/config.yaml", "r", encoding="utf-8") as f:
        return yaml.safe_load(f)