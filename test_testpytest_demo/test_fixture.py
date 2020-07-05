#!/usr/bin/env python
# encoding: utf-8
import pytest


class TestLogin:
    def test_case01(self, login):
        print("testcase 1")
        print(login())

    @pytest.mark.usefixtures('login')
    def test_case2(self):
        print("testcase 2")
