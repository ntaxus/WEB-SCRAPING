from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver


def setup_driver():
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(s.path)

    return driver