#!/usr/bin/env python
# encoding: utf-8
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage():
    _base_url = ""

    def __init__(self, driver_basepage: WebDriver = None):
        # 判断driver是否实例话，没有则生成，有则复用
        if driver_basepage == None:
            option = Options()
            # Google\ Chrome --remote -debugging-port=9223
            option.debugger_address = "localhost:9223"
            self.driver = webdriver.Chrome(options=option)
        else:
            self.driver = driver_basepage
        # 判断是否有地址，没有则调用子类中的url
        if self._base_url != "":
            self.driver.get(self._base_url)
        # 显示等待driver生成五秒
        self.driver.implicitly_wait(5)

    def find(self, by, value):
        # 查找元素，将seleium方法和功能解耦
        return self.driver.find_element(by=by, value=value)

    def finds(self, by, value):
        # 查找多组元素
        return self.driver.find_elements(by=by, value=value)

    def quit(self):
        # 关闭driver
        self.driver.quit()

    def wait(self, timeout, local):
        # 封装显示等待
        return WebDriverWait(self.driver, timeout, poll_frequency=0.5) \
            .until(EC.presence_of_element_located(local))
