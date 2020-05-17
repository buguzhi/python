from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from web.selenium_test.page_object.selenium_wework_main.page.add_member import AddMember


class Main:
    def __init__(self):
        options = Options()
        options.debugger_address = '127.0.0.1:9222'
        self.deriver = webdriver.Chrome(options=options)
        self.deriver.get("https://work.weixin.qq.com/wework_admin/frame")

    def goto_add_member(self):
        #click add member
        self._driver.find_element(By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(1)').click()
        return AddMember(self.deriver)