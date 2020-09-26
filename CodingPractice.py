from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C://chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(4)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_link_text("Shop").click()
products = driver.find_elements_by_xpath("//div[@class='card h-100']")
for product in products:
    productname = product.find_element_by_xpath("div/h4/a").text
    if productname == "Blackberry":
        product.find_element_by_xpath("div[2]/button").click()
driver.find_element_by_css_selector("a[class='nav-link btn btn-primary']").click()
driver.find_element_by_css_selector("button[class='btn btn-success']").click()
driver.find_element_by_id("country").send_keys("ind")
wait = WebDriverWait(driver, 7)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element_by_link_text("India").click()
driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
driver.find_element_by_xpath("//input[@type='submit']").click()
successtext = driver.find_element_by_xpath("//div[@class='alert alert-success alert-dismissible']").text
assert "Success" in successtext
driver.get_screenshot_as_file('screen.png')