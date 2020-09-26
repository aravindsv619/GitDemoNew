import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import Homepage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        log = self.getlogger()

        homepage = Homepage(self.driver)
        log.info("first name is"+(getData["firstname"]))
        homepage.getName().send_keys(getData["firstname"])
        homepage.getEmail().send_keys(getData["email"])
        homepage.getcheckBox().click()
        self.SelectOptionByText(homepage.getGender(), getData["gender"])
        homepage.SubmitButton().click()
        message = homepage.SuccessMessage().text
        assert ("Success" in message)
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.getTestData("Testcase2"))
    def getData(self, request):
        return request.param
