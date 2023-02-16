import os
from colorama import Fore
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

driver = None
_wait = None

def start_driver():
    '''
    Starts the web driver and defines selenium_helper.driver.
    '''
    global driver
    global _wait
    
    # hide webdriver_manager logs:
    os.environ['WDM_LOG_LEVEL'] = '0'

    # create service object:
    _service = Service(ChromeDriverManager().install())

    # disable image loading for better performance:
    _chrome_options = webdriver.ChromeOptions()
    _chrome_options.experimental_options["prefs"] = {
        "profile.default_content_settings": {"images": 2},
        "profile.managed_default_content_settings": {"images": 2}
    }

    # hide selenium logs:
    _chrome_options.add_argument("--log-level=3")

    # create WebDriver
    driver = webdriver.Chrome(service=_service, chrome_options=_chrome_options)

    # maximize window
    driver.maximize_window()

    _wait = WebDriverWait(driver, 5, ignored_exceptions=(NoSuchElementException,StaleElementReferenceException))