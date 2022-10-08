from selenium import webdriver
import pytest

@pytest.fixture()
def setup():
    driver=webdriver.Chrome(executable_path='C:\\Users\\preet\\OneDrive\\Desktop\\driver\\chromedriver.exe')
    return driver

#########Generate HTML report##############
def pytest_configure(config):
    config._metadata['Project Name'] = 'NOP commerse'
    config._metadata['Module name'] = 'Login'
    config._metadata['Tester']='Preethi'