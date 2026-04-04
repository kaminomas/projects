from pages.login_page import LoginPage


def test_login(driver):
    login_page = LoginPage(driver)
    login_page.login("tomsmith", "SuperSecretPassword!")
    assert "secure" in driver.current_url

