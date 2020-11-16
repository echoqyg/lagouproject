#!/usr/bin/env python
# encoding: utf-8
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.options import Options

from test_wework.page.main_page import MainPage


class TestAddMember:

    def setup(self):
        self.main = MainPage()

    def test_add_member(self):
        # 1.点击添加成员，跳转添加成员页面2.填写成员信息3.点击保存4.进行校验
        assert "钱钱" in self.main.goto_add_member().add_member().get_member()

    def test_add_member_fail(self):
        # 1.点击添加成员，跳转添加成员页面2.填写成员信息3.点击保存点击取消4.进行校验
        assert "钱钱1" not in self.main.goto_add_member().add_member_fail().get_member()

    def test_add_member_by_file(self):
        # 1、点击导入通讯录，跳转至通讯录页面2、点击上传文件，并上传data中的模版、点击导入，点击完成，跳转到成员页面5、进行校验
        assert "张三（示例）" in self.main.goto_import_contact().upload_file().get_member()

    def teardown(self):
        self.main.quit()
