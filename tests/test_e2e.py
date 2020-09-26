from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckoutPage import CheckOutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import Homepage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getlogger()
        homepage = Homepage(self.driver)
        checkoutpage = homepage.shopItems()
        log.info("getting all the cart titles")

        product = checkoutpage.productFromList()
        for item in product:

            producttext = item.text
            if producttext == "Blackberry":
                checkoutpage.getNameFooter().click()
        checkoutpage.checkoutItems().click()
        checkoutpage.checkoutConfirmSuccess().click()
        log.info("Entering country name as Ind")
        checkoutpage.countrySelectFromList().send_keys("ind")
        self.verifyLinkPresence("India")
        checkoutpage.CountrySelectIndia().click()
        checkoutpage.checkBox().click()
        checkoutpage.purchase().click()

        confirmpage = ConfirmPage(self.driver)
        successmessage = confirmpage.successMessage().text
        log.info("Text received from application is " + successmessage)
        assert "Success! Thank you!" in successmessage
