from selenium import webdriver
from selenium.webdriver.common.by import By

from web.selenium_test.page_object.selenium_wework_login.login import Login
from web.selenium_test.page_object.selenium_wework_login.register import Register


class Idex:
    def goto_login(self):
        # click login
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/")
        self.driver.find_element(By.CSS_SELECTOR,"")
        return Login()
    def goto_register(self):
        # click register
        return Register()


