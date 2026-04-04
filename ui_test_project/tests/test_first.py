from selenium import webdriver
def test_first():
    driver = webdriver.Remote(
        command_executor="http://localhost:4444/wd/hub",
        options=webdriver.ChromeOptions()
        )

    driver.get("http://the-internet.herokuapp.com/")

    assert "The Internet" in driver.title
    driver.quit()