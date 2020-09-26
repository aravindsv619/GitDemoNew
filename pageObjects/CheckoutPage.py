from selenium.webdriver.common.by import By


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    productName = (By.XPATH, "//div[@class='card h-100']/div/h4/a")
    productNameFooter = (By.XPATH, "//div[@class='card h-100']/div[2]/button")
    checkoutButton = (By.XPATH, "//a[@class='nav-link btn btn-primary']")
    checkoutConfirm = (By.XPATH, "//button[@class='btn btn-success']")
    countrySelect = (By.ID, "country")
    countryIndia = (By.LINK_TEXT, "India")
    checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    purchaseButton = (By.XPATH, "//input[@type='submit']")

    def productsFromList(self):
        return self.driver.find_elements(*CheckOutPage.productsName)

    def productFromList(self):
        return self.driver.find_elements(*CheckOutPage.productName)

    def getNameFooter(self):
        return self.driver.find_element(*CheckOutPage.productNameFooter)

    def checkoutItems(self):
        return self.driver.find_element(*CheckOutPage.checkoutButton)

    def checkoutConfirmSuccess(self):
        return self.driver.find_element(*CheckOutPage.checkoutConfirm)

    def countrySelectFromList(self):
        return self.driver.find_element(*CheckOutPage.countrySelect)

    def CountrySelectIndia(self):
        return self.driver.find_element(*CheckOutPage.countryIndia)

    def checkBox(self):
        return self.driver.find_element(*CheckOutPage.checkbox)

    def purchase(self):
        return self.driver.find_element(*CheckOutPage.purchaseButton)
