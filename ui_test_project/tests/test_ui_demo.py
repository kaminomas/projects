import time
def test_open_home(driver, config_data):
    print(type(driver))
    print(driver)
    driver.get(config_data["base_url"])
    time.sleep(10)
    assert "learnblockchain" in driver.current_url