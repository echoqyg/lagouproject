#!/usr/bin/env python
# encoding: utf-8
import pytest
import yaml

from test_appium.test_wechat.page.app import App


class TestWework:
    def setup_class(self):
        self.app = App()
        self.main = self.app.start().main()

    @pytest.mark.parametrize("contact_data", yaml.safe_load(
        open("/Users/xiaohui/PycharmProjects/lagouproject/test_appium/test_wechat/contacts.yml")))
    def test_addcontact(self, contact_data):
        name = contact_data['name']
        gender = contact_data['gender']
        iphone = contact_data['iphone']
        toast = self.main.goto_address_list().click_addmember() \
            .addmember_menual().edit_username(name).edit_gender(gender).edit_phonenum(iphone).click_save().get_result()
        assert "添加成功" == toast
        self.main.back()

    @pytest.mark.parametrize("name", yaml.safe_load(
        open("/Users/xiaohui/PycharmProjects/lagouproject/test_appium/test_wechat/del_contacts.yml")))
    def test_delcontact(self, name):
        names = self.main.goto_address_list().click_contact(
            name).click_setting().click_contact_edit().click_delete().click_affirm().get_texts(name)
        assert name not in names

    def teardown_class(self):
        self.app.close()
