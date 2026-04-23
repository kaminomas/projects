import os
import time

import pytest


@pytest.mark.skipif(
    os.environ.get("SELENIUM_HUB_RUNNING") != "1",
    reason="Requires a running Selenium Grid at localhost:4444 "
    "(start via docker-compose.yml, then set SELENIUM_HUB_RUNNING=1).",
)
def test_open_home(driver, config_data):
    driver.get(config_data["base_url"])
    time.sleep(10)
    assert "learnblockchain" in driver.current_url
