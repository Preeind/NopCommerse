import pytest
from selenium import webdriver
from Pages.LoginPage import Login
from Utilities.readproperties import ReadConfig
from Utilities.customlogger import LogGeneration

class Test_Login_01:
    baseURL = ReadConfig.getApplicationURL()
    email = ReadConfig.getemail()
    password = ReadConfig.getpassword()

    logger=LogGeneration.LogGeneration()

    def test_homepage_title(self,setup):
        self.logger.info("**********Verifying home page title in TC_01**********")

        self.driver=setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        self.driver.close()
        if act_title=="nopCommerce demo store. Login":
            assert True
            self.driver.close()
            self.logger.info("******TC01 is passed****")
        else:
            assert False

    def test_login(self,setup):
        self.logger.info("*********Verify valid login********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=Login(self.driver)
        self.lp.click_login_login()
        self.lp.setemail(self.email)
        self.lp.setpassword(self.password)
        self.lp.click_login()
        self.logger.info("********Login TC is passed********")


