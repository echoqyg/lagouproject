#!/usr/bin/env python
# encoding: utf-8
# 成员编辑页面
from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from test_appium.test_wechat.page.base_page import BasePage


class ContactAddPage(BasePage):
    _send_username = (MobileBy.XPATH, "//*[contains(@text,'姓名')]/../android.widget.EditText")
    _click_gender = (MobileBy.XPATH, "//*[@text='性别']/..//*[@text='男']")
    _click_male = (MobileBy.XPATH, "//*[@text='男']")
    _click_female = (MobileBy.XPATH, "//*[@text='女']")
    _send_phonenum = (MobileBy.XPATH, "//*[contains(@text,'手机')]/..//*[@text='手机号']")
    _click_save = (MobileBy.XPATH, "//*[@text='保存']")

    def edit_username(self, name):
        self.find(self._send_username).send_keys(
            name)
        return self

    def edit_gender(self, gender):
        self.find_and_click(self._click_gender)
        self.driver.implicitly_wait(3)
        if gender == "女":
            self.find_and_click(self._click_female)
            self.driver.implicitly_wait(2)
        else:
            self.find_and_click(self._click_male)
            self.driver.implicitly_wait(2)
        return self

    def edit_phonenum(self, phonenum):
        self.find(self._send_phonenum).send_keys(
            phonenum)
        return self

    def click_save(self):
        self.find_and_click(self._click_save)
        sleep(2)
        from test_appium.test_wechat.page.memberinvite_page import MemberInvitePage
        return MemberInvitePage(self.driver)
