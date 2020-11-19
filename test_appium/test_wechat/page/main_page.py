#!/usr/bin/env python
# encoding: utf-8
# 主页面
from appium.webdriver.common.mobileby import MobileBy
from test_appium.test_wechat.page.base_page import BasePage


class MainPage(BasePage):
    _click_addressList = (MobileBy.XPATH, "//*[@text='通讯录']")

    def goto_address_list(self):
        from test_appium.test_wechat.page.address_list_page import AddressListPage
        self.find_and_click(self._click_addressList)
        return AddressListPage(self.driver)

    def goto_message(self):
        pass

    def goto_workbench(self):
        pass
