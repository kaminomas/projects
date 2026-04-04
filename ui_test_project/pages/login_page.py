from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class LoginPage:
    def __init__(self, driver):
        self.driver = driver


    def login(self, username, password):
        self.driver.get("http://the-internet.herokuapp.com/login")
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        element.clear()
        element.send_keys(username)

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "password"))
        )
        element.clear()
        element.send_keys(password)

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']"))
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.url_contains("/secure")
        )


