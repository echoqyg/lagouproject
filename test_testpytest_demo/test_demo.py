#!/usr/bin/env python
# encoding: utf-8
import pytest
import yaml

from test_testpytest_demo.cal import Calculator


def setup_module():
    print("==========setup_module")


def teardown_module():
    print("teardown_module")


def setup_function():
    print("setup_function")


def teardown_function():
    print("teardown_function")


# def test_a():
#     assert 1 == 1
# def test_b():
#     assert 1 == 1

class Test_cal:
    def setup_class(self):
        self.cal = Calculator()
        print("setup_class")

    def teardowm_class(self):
        print("setup_class")

    def setup(self):
        print("开始计算")
        print("setup")

    def teardown(self):
        print("结束计算")

    @pytest.mark.parametrize('a,b,result', yaml.safe_load(open("./data.yml"))["add"])
    def test_add(self, a, b, result):
        assert result == self.cal.add(a, b)

    @pytest.mark.parametrize('a,b,result', yaml.safe_load(open("./data.yml"))["sub"])
    def test_sub(self, a, b, result):
        assert result == self.cal.sub(a, b)

    @pytest.mark.parametrize('a,b,result', yaml.safe_load(open("./data.yml"))["mul"])
    def test_mul(self, a, b, result):
        assert result == self.cal.mul(a, b)

    @pytest.mark.parametrize('a,b,result', yaml.safe_load(open("./data.yml"))["div"])
    def test_div(self, a, b, result):
        assert result == self.cal.div(a, b)
