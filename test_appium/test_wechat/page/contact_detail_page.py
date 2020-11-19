#!/usr/bin/env python
# encoding: utf-8
from appium.webdriver.common.mobileby import MobileBy

from test_appium.test_wechat.page.base_page import BasePage


class ContactDetailPage(BasePage):
    _setting = (MobileBy.XPATH, "//*[@text='个人信息']/../../../../..//*["
                                "@resource-id='com.tencent.wework:id/i6r']")

    def click_setting(self):
        self.find_and_click(self._setting)
        from test_appium.test_wechat.page.contactdetail_setting_page import ContactDetailSettingPage
        return ContactDetailSettingPage(self.driver)
