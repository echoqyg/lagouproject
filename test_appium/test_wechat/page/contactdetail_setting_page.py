#!/usr/bin/env python
# encoding: utf-8
from appium.webdriver.common.mobileby import MobileBy

from test_appium.test_wechat.page.base_page import BasePage


class ContactDetailSettingPage(BasePage):
    _set_contact = (MobileBy.XPATH, "//*[@text='编辑成员']")

    def click_contact_edit(self):
        self.find_and_click(self._set_contact)
        from test_appium.test_wechat.page.contactedit_page import ContactEditPage
        return ContactEditPage(self.driver)
