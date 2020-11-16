#!/usr/bin/env python
# encoding: utf-8

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestLogin:
    def test_debug_login(self):
        option = Options()
        # Google\ Chrome --remote-debugging-port=9223
        option.debugger_address = "localhost:9223"
        driver = webdriver.Chrome(options=option)
        driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
