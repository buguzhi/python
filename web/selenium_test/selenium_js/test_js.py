from time import sleep

from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By

from web.selenium_test.selenium_js.base import Base


class TestJs(Base):
    @pytest.mark.skip
    def test_js_scroll(self):
        self.driver.get("http://www.baidu.com")
        self.driver.find_element(By.ID, "kw").send_keys("selenium测试")
        element = self.driver.execute_script("return document.getElementById('su')")
        element.click()
        self.driver.execute_script("document.documentElement.scrollTo=10000")
        sleep(3)
        for code in [
            'return document.title', 'return JSON.stringify(performance.timing)'
        ]:
            print(self.driver.execute_script(code))

    def test_dateltime(self):
        self.driver.get("https://www.12306.cn/index/")
        time_element = self.driver.execute_script("a=document.getElementById('train_date');a.removeAttribute('readonly')")
        self.driver.execute_script("document.getElementById('train_date').value='2020-12-30'")
        sleep(3)
        print(self.driver.execute_script("return a = document.getElementById('train_date').value"))


if __name__ == '__main__':
    pytest.main()
