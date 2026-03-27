from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def create_remote_driver(command_executor: str):
    options = Options()
    options.add_argument("--window-size=1440,900")

    driver = webdriver.Remote(
        command_executor=command_executor,
        options=options
    )
    return driver