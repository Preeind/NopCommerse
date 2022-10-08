from selenium import webdriver
from selenium.webdriver.common.by import By


class Login:
    btn_login_login_xath = "//a[@href='/login?returnUrl=%2F']"
    txt_email_xpath = "//input[@class='email']"
    txt_password_xpath = "//input[@class='password']"
    btn_login_xpath = "//*[contain(text(),'Log in']"

    ##initialize the constructor for this class

    def __init__(self,driver):
        self.driver=driver

    def setemail(self,email):
        self.driver.find_element(by=By.XPATH, value="/html/body/div[6]/div[3]/div/div/div/div[2]/div[1]/div[2]/form/div[2]/div[1]/input").send_keys(email)
        #self.driver.find_element_by_xpath(self.txt_email_xpath).sendkeys(email)

    def setpassword(self,password):
        self.driver.find_element(by=By.XPATH, value="/html/body/div[6]/div[3]/div/div/div/div[2]/div[1]/div[2]/form/div[2]/div[2]/input").send_keys(password)
        #self.driver.find_element_by_xpath(self.txt_password_xpath).sendkeys(password)

    def click_login_login(self):
        self.driver.find_element(by=By.XPATH, value="//a[@href='/login?returnUrl=%2F']").click()
        #self.driver.find_element_by_xpath(self.btn_login_login_xath).click()

    def click_login(self):
        self.driver.find_element(by=By.XPATH, value="/html/body/div[6]/div[3]/div/div/div/div[2]/div[1]/div[2]/form/div[3]/button").click()
        #self.driver.find_element_by_xpath(self.btn_login_xpath).click()