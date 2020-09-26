from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--disable-notifications")
options.headless = True
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(executable_path="C://chromedriver.exe")

url = "https://www.justdial.com/Delhi/S-K-Premium-Par-Hari-Nagar/011PXX11-XX11-131128122154-B8G6_BZDET"
driver.get(url)

pop_up = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="best_deal_detail_div"]/section/span')))
time.sleep(2.5)
pop_up.click()  # For disable pop-up

while True:
    try:
        element = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Load More Reviews..']")))
        element.click()

    except TimeoutException:
        break

    except:
        pass
print([span.text for span in driver.find_elements_by_css_selector('span.rName.lng_commn')])
driver.close()