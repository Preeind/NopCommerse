import time

import pytest
from selenium import webdriver
from Pages.LoginPage import Login
from Utilities.readproperties import ReadConfig
from Utilities.customlogger import LogGeneration
from Utilities import XLUtils

class Test_Login_DDT_02:
    path=".//Testdata/LoginTestdata.xlsx"
    baseURL = ReadConfig.getApplicationURL()
    email = ReadConfig.getemail()
    password = ReadConfig.getpassword()

    logger=LogGeneration.LogGeneration()

    def test_login_DDT(self,setup):
        self.logger.info("********DDT Test********")
        self.logger.info("*********Verify valid login********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=Login(self.driver)

        self.rows=XLUtils.getRowCount(self.path,'Sheet1')
        print("Number of Rows in Excel",self.rows)

        for r in range(2,self.rows+1):
            self.email= XLUtils.readData(self.path,'Sheet1',r,1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r,2)
            self.expected = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.click_login_login()
            self.lp.setemail(self.email)
            self.lp.setpassword(self.password)
            self.lp.click_login()
            time.sleep(5)

            act_title=self.driver.title
            expected_title="nopCommerce demo store. Login"


