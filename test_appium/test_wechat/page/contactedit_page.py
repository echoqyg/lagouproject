#!/usr/bin/env python
# encoding: utf-8
from appium.webdriver.common.mobileby import MobileBy

from test_appium.test_wechat.page.base_page import BasePage


class ContactEditPage(BasePage):
    _click_affirm = (MobileBy.XPATH, "//*[@text='确定']")

    def click_delete(self):
        self.find_by_scroll("删除成员").click()
        return self

    def click_affirm(self):
        self.find_and_click(self._click_affirm)
        from test_appium.test_wechat.page.address_list_page import AddressListPage
        return AddressListPage(self.driver)
