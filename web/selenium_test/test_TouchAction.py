from time import sleep

from selenium import webdriver
from selenium.webdriver import TouchActions
from selenium.webdriver.common.by import By
import pytest

class TestTouchAction():
    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c',False)
        self.driver=webdriver.Chrome(options=option)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_touchaction_scrollbotton(self):

        self.driver.get("http://www.baidu.com")
        el = self.driver.find_element(By.ID,"kw")
        el_search = self.driver.find_element(By.ID,"su")
        el.send_keys("selenium测试")
        action = TouchActions(self.driver)
        action.tap(el_search)
        action.perform()
        action.scroll_from_element(el,0,10000).perform()
        sleep(3)
