from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckOutPage


class Homepage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.LINK_TEXT, "Shop")
    name = (By.CSS_SELECTOR, "input[name='name']")
    email = (By.NAME, "email")
    checkbox = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    submitbutton = (By.XPATH, "//input[@type='submit']")
    successmessage = (By.CLASS_NAME, "alert-success")

    def shopItems(self):
        self.driver.find_element(*Homepage.shop).click()
        checkoutpage = CheckOutPage(self.driver)
        return checkoutpage

    def getName(self):
        return self.driver.find_element(*Homepage.name)

    def getEmail(self):
        return self.driver.find_element(*Homepage.email)

    def getcheckBox(self):
        return self.driver.find_element(*Homepage.checkbox)

    def getGender(self):
        return self.driver.find_element(*Homepage.gender)

    def SubmitButton(self):
        return self.driver.find_element(*Homepage.submitbutton)

    def SuccessMessage(self):
        return self.driver.find_element(*Homepage.successmessage)
