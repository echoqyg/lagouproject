#!/usr/bin/env python
# encoding: utf-8
# 通讯录页面
from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

from test_appium.test_wechat.page.base_page import BasePage


class AddressListPage(BasePage):
    _click_addContact = "添加成员"

    # 添加成员
    def click_addmember(self):
        self.find_by_scroll(self._click_addContact).click()
        from test_appium.test_wechat.page.memberinvite_page import MemberInvitePage
        return MemberInvitePage(self.driver)

    def click_contact(self, name):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='%s']" % name).click()
        from test_appium.test_wechat.page.contact_detail_page import ContactDetailPage
        return ContactDetailPage(self.driver)

    def get_texts(self, name):
        WebDriverWait(self.driver, 30).until_not(lambda x: x.find_element_by_xpath("//*[@text='%s']" % name))
        name_elements: list[WebElement] = self.driver.find_elements_by_xpath(
            "//*[@text='添加成员']/../../../../../..//*[@text!='']")
        names = []
        [names.append(name_element.text) for name_element in name_elements]
        print(names)
        return names
