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

# create service object:
_service = Service(ChromeDriverManager().install())

# create WebDriver
driver = webdriver.Chrome(service=_service)

driver.get('http://127.0.0.1:5500/site.html')

driver.switch_to.frame(0)

all_boxes = []
iterations = 0
limit = 10

while iterations < limit:
    boxes = driver.find_elements_by_css_selector('div.box1')
    new_boxes = [b for b in boxes if b.id not in [ab.id for ab in all_boxes]]
    all_boxes.extend(new_boxes)
    driver.execute_script('arguments[0].scrollIntoView({block: "center"})', new_boxes[-1])

    sleep(4)

print(len(all_boxes))
    