#!/usr/bin/env python
# encoding: utf-8
from selenium.webdriver.common.by import By

from test_wework.page.base_page import BasePage
from test_wework.page.contact_page import Contact


class ImportContact(BasePage):

    def upload_file(self):
        self.find(By.CSS_SELECTOR, ".ww_fileImporter_fileContainer_uploadInputMask") \
            .send_keys("/Users/xiaohui/PycharmProjects/lagouproject/test_wework/data/test.xlsx")
        self.find(By.CSS_SELECTOR, ".ww_fileImporter_submit").click()
        self.wait(5, (By.CSS_SELECTOR, ".ww_fileImporter_successImportText"))
        self.find(By.CSS_SELECTOR, ".ww_btn_Big").click()
        return Contact(self.driver)
