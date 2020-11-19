#!/usr/bin/env python
# encoding: utf-8
from time import sleep

import pytest
import yaml
from appium import webdriver
from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait


class TestWechatWork:
    def setup_class(self):
        caps = {
            "platformName": "Android",
            "deviceName": "emulator-5554",
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.WwMainActivity",
            "noReset": "true",
            "unicodeKeyboard": "true",
            "dontStopAppOnReset": "true",
            "skipDeviceInitialization": "true",
            "automationName": 'uiautomator2'
        }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def teardown_class(self):
        self.driver.quit()

    @pytest.mark.parametrize("contact_data", yaml.safe_load(
        open("/Users/xiaohui/PycharmProjects/lagouproject/test_appium/test/contacts.yml")))
    def test_add_contact(self, contact_data: dict):
        name = contact_data['name']
        gender = contact_data['gender']
        iphone = contact_data['iphone']
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys(
            name)
        self.driver.implicitly_wait(3)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='性别']/..//*[@text='男']").click()
        self.driver.implicitly_wait(3)
        if gender == "女":
            self.driver.find_element_by_xpath("//*[@text='女']").click()
            self.driver.implicitly_wait(2)
        else:
            self.driver.find_element_by_xpath("//*[@text='男']").click()
            self.driver.implicitly_wait(2)
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'手机')]/..//*[@text='手机号']").send_keys(
            iphone)
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_xpath("//*[@text='保存']").click()
        sleep(3)
        toast_text = self.driver.find_element_by_xpath("//*[@class='android.widget.Toast']").text
        sleep(2)
        self.driver.find_element_by_xpath(
            "//*[@text='添加成员']/../../../..//*[@resource-id='com.tencent.wework:id/i63']").click()
        self.driver.find_element_by_xpath("//*[@text='消息']").click()
        assert "添加成功" == toast_text

    @pytest.mark.parametrize("name", yaml.safe_load(
        open("/Users/xiaohui/PycharmProjects/lagouproject/test_appium/test/del_contacts.yml")))
    def test_del_contact(self, name):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.driver.implicitly_wait(2)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='%s']" % name).click()
        self.driver.implicitly_wait(2)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='个人信息']/../../../../..//*["
                                                 "@resource-id='com.tencent.wework:id/i6r']").click()
        self.driver.implicitly_wait(2)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='编辑成员']").click()
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).'
            'scrollIntoView(new UiSelector().text("删除成员").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='确定']").click()
        WebDriverWait(self.driver, 30).until_not(lambda x: x.find_element_by_xpath("//*[@text='%s']" % name))
        name_elements: list[WebElement] = self.driver.find_elements_by_xpath(
            "//*[@text='添加成员']/../../../../../..//*[@text!='']")
        names = []
        [names.append(name_element.text) for name_element in name_elements]
        sleep(2)
        self.driver.find_element_by_xpath("//*[@text='消息']").click()
        assert name not in names
