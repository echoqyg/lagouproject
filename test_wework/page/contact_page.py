#!/usr/bin/env python
# encoding: utf-8
import time

from selenium.webdriver.common.by import By
from test_wework.page.base_page import BasePage


class Contact(BasePage):

    def get_member(self):
        time.sleep(1)
        elements = self.finds(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        return [element.get_attribute("title") for element in elements]

    def delete_all_member(self):
        # 点击姓名旁多选框
        # 这里不加等待就报错，显示等待不知道找什么元素下面三个元素都试了，不行
        time.sleep(1)
        self.finds(By.CSS_SELECTOR, ".ww_checkbox").pop(0).click()
        # 判断是否选中
        if self.finds(By.CSS_SELECTOR, ".ww_checkbox").pop(0).is_selected():
            # 点击删除
            self.find(By.CSS_SELECTOR, ".js_delete").click()
            # 点击确认
            self.finds(By.CSS_SELECTOR, ".ww_btn_Blue").pop().click()
            return Contact(self.driver)
