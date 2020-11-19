#!/usr/bin/env python
# encoding: utf-8
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_and_click(self, locator):
        return self.find(locator).click()

    def find_by_scroll(self, text):
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                        'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                                        '.scrollIntoView(new UiSelector().text("%s").instance(0));' % text)

    def back(self, num=1):
        for i in range(num):
            self.driver.back()
