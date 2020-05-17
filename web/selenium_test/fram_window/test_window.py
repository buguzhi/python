from time import sleep

from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By

from web.selenium_test.fram_window.base import Base


class TestWindows(Base):
    def test_window(self):
        self.driver.get("http://www.baidu.com")
        self.driver.find_element(By.LINK_TEXT, "登录").click()
        print(self.driver.current_window_handle)
        self.driver.find_element(By.LINK_TEXT, "立即注册").click()
        print(self.driver.current_window_handle)
        print(self.driver.window_handles)
        windows = self.driver.window_handles
        self.driver.switch_to_window(windows[-1])
        self.driver.find_element(By.ID, "TANGRAM__PSP_4__userName").send_keys("123456")
        self.driver.find_element(By.ID, "TANGRAM__PSP_4__phone").send_keys("45678")
        self.driver.switch_to_window(windows[-2])

        self.driver.find_element(By.ID, "TANGRAM__PSP_10__footerULoginBtn").click()
        self.driver.find_element(By.ID, "TANGRAM__PSP_10__userName").send_keys("123456")
        self.driver.find_element(By.ID, "TANGRAM__PSP_10__password").send_keys("123456")
        sleep(3)


if __name__ == '__main__':
    pytest.main()
