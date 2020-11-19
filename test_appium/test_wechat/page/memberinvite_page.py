#!/usr/bin/env python
# encoding: utf-8
# 添加成员也
from appium.webdriver.common.mobileby import MobileBy
from test_appium.test_wechat.page.base_page import BasePage


class MemberInvitePage(BasePage):
    _click_member = (MobileBy.XPATH, "//*[@text='手动输入添加']")
    _get_toast = (MobileBy.XPATH, "//*[@class='android.widget.Toast']")

    def addmember_menual(self):
        self.find_and_click(self._click_member)
        from test_appium.test_wechat.page.contact_add_page import ContactAddPage
        return ContactAddPage(self.driver)

    def get_result(self):
        return self.find(self._get_toast).text
