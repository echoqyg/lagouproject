#!/usr/bin/env python
# encoding: utf-8
import pytest
import re
from api.tag import TagApi
from api.wework import WeWork


class TestTag:
    @pytest.fixture(scope="session")
    def token(self):
        yield WeWork().test_get_token()

    def setup(self):
        self.tag = TagApi()

    def create_muti_data(self):
        data = [("yuuu123yu" + str(x), str(x)) for x in range(1, 4)]
        return data

    @pytest.mark.parametrize("tagname,tagid", create_muti_data("xx"))
    def test_all(self, tagname, tagid, token):
        assert "created" == self.tag.test_create(tagname, tagid, token)['errmsg']
        assert "ok" == self.tag.test_getlist(token)['errmsg']
        assert "updated" == self.tag.test_update(tagname + tagid, tagid, token)['errmsg']
        assert "deleted" == self.tag.test_delete(tagid, token)['errmsg']

    # @pytest.mark.parametrize("tagname,tagid", create_muti_data("xx"))
    # def test_create(self, tagname, tagid, token):
    #     assert "created" == self.tag.test_create(tagname, tagid, token)['errmsg']
    #
    # def test_getlist(self, token):
    #     print(self.tag.test_getlist(token)['taglist'])
    #
    # @pytest.mark.parametrize("tagname,tagid", create_muti_data("xx"))
    # def test_update(self, tagname, tagid, token):
    #     print(self.tag.test_update(tagname + tagid, tagid, token)['errmsg'])
    #
    # @pytest.mark.parametrize("tagid", ["23", "33"])
    # def test_deleted(self, tagid, token):
    #     assert "deleted" == self.tag.test_delete(tagid, token)['errmsg']
