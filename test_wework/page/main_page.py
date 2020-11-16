#!/usr/bin/env python
# encoding: utf-8

from selenium.webdriver.common.by import By

from test_wework.page.importContact_page import ImportContact
from test_wework.page.addMember_page import AddMember
from test_wework.page.contact_page import Contact
from test_wework.page.base_page import BasePage


class MainPage(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def goto_add_member(self):
        # 跳转函数名可以命名为goto
        # click
        self.find(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(1)").click()
        return AddMember(self.driver)

    def goto_contact(self):
        self.find(By.ID, "menu_contacts").click()
        return Contact(self.driver)

    def goto_import_contact(self):
        self.find(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)").click()
        return ImportContact(self.driver)
