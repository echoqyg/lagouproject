#!/usr/bin/env python
# encoding: utf-8
from test_wework.page.main_page import MainPage


class TestDeleteMember:
    def setup(self):
        self.main = MainPage()

    def test_delete_member(self):
        # 1点击通讯录,跳转通讯录 2、找到姓名对应的单选框勾选 3、点击删除 4、点击确认 5、验证是否删除
        assert len(self.main.goto_contact().delete_all_member().get_member()) == 1
