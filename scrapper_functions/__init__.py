from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver


def setup_driver():
    '''
    Inicializamos el web driver de selenium

    :return: driver
    '''
    s = Service(ChromeDriverManager().install())
    return webdriver.Chrome(s.path)