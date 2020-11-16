#!/usr/bin/env python
# encoding: utf-8

from selenium.webdriver.common.by import By

from test_wework.page.contact_page import Contact
from test_wework.page.base_page import BasePage


class AddMember(BasePage):
    _username = "username"
    _memberAdd_acctid = "memberAdd_acctid"
    _memberAdd_phone = "memberAdd_phone"
    _js_btn_save = ".js_btn_save"

    def add_member(self):
        """
        添加成员
        :return:
        """
        self.wait(5, (By.ID, self._memberAdd_phone))
        self.find(By.ID, self._username).send_keys("钱钱")
        self.find(By.ID, self._memberAdd_acctid).send_keys("12345")
        self.find(By.ID, self._memberAdd_phone).send_keys("13011111111")
        self.find(By.CSS_SELECTOR, self._js_btn_save).click()
        return Contact(self.driver)

    def add_member_fail(self):
        """
        添加成员
        :return:
        """
        self.wait(5, (By.ID, self._memberAdd_phone))
        self.find(By.ID, self._username).send_keys("钱钱1")
        self.find(By.ID, self._memberAdd_acctid).send_keys("12345")
        self.find(By.ID, self._memberAdd_phone).send_keys("13011121111")
        self.find(By.CSS_SELECTOR, self._js_btn_save).click()
        self.find(By.CSS_SELECTOR, ".js_btn_cancel").click()
        return Contact(self.driver)
