from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class TestActionChains:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_case_click(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        element_click = self.driver.find_element(By.XPATH, "//input[@value='click me']")
        element_doubleclick = self.driver.find_element(By.XPATH, "//input[@value='dbl click me']")
        element_rightclick = self.driver.find_element(By.XPATH, "//input[@value='right click me']")
        action = ActionChains(self.driver)
        action.click(element_click)
        action.context_click(element_rightclick)
        action.double_click(element_doubleclick)
        sleep(3)
        action.perform()
        sleep(3)

    @pytest.mark.skip
    def test_movetoeleminet(self):
        self.driver.get("http://www.baidu.com/")
        element = self.driver.find_element(By.ID, "s-usersetting-top")
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()
        sleep(3)

    def test_dragdriop(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        drag_element = self.driver.find_element(By.ID, "dragger")
        drop_element = self.driver.find_element(By.XPATH, "/html/body/div[2]")
        action = ActionChains(self.driver)
        action.drag_and_drop(drag_element, drop_element).perform()
        sleep(3)
        action.click_and_hold(drag_element).move_to_element(drop_element).release().perform()

if __name__ == '__main__':
    pytest.main()
