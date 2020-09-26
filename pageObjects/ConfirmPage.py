from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    successText = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    def successMessage(self):
        return self.driver.find_element(*ConfirmPage.successText)
