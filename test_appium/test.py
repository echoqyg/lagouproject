#!/usr/bin/env python

import time
from appium import webdriver

disired_caps = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "appPackage": "com.android.browser",
    "appActivity": ".BrowserActivity",
    "noReset": True
}
driver = webdriver.Remote("http://localhost:4723/wd/hub", disired_caps)
driver.implicitly_wait(5)
el1 = driver.find_element_by_id("com.android.browser:id/url")
el1.click()  #
el1.send_keys("https://www.baidu.com")
driver.press_keycode(66)  # search 84，enter,66
time.sleep(5)
