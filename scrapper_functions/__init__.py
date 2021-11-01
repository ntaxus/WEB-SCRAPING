from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


def setup_driver():
    '''
    Inicializamos el web driver de selenium

    :return: driver
    '''

    # Inicializamos User-Agent que queremos
    opts = Options()
    opts.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                      "AppleWebKit/537.36 (KHTML, like Gecko)"
                      "Chrome/95.0.4638.54 Safari/537.36")

    # Setup del webdriver
    s = Service(ChromeDriverManager().install())
    return webdriver.Chrome(s.path, chrome_options=opts)