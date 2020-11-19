#!/usr/bin/env python
# encoding: utf-8
from appium import webdriver
from appium.webdriver.webdriver import WebDriver

from test_appium.test_wechat.page.base_page import BasePage


class App(BasePage):
    driver: WebDriver

    def start(self):
        if self.driver is None:
            caps = {
                "platformName": "Android",
                "deviceName": "emulator-5554",
                "appPackage": "com.tencent.wework",
                "appActivity": ".launch.WwMainActivity",
                "noReset": "true",
                "unicodeKeyboard": "true",
                # "dontStopAppOnReset": "true",
                # "skipDeviceInitialization": "true",
                "automationName": 'uiautomator2'
            }
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        else:
            self.driver.launch_app()
        self.driver.implicitly_wait(10)
        return self

    def restart(self):
        self.driver.quit()
        self.start()

    def close(self):
        self.driver.quit()

    def main(self):
        from test_appium.test_wechat.page.main_page import MainPage
        return MainPage(self.driver)
