#!/usr/bin/env python
# encoding: utf-8
import pytest

from test_testpytest_demo.cal import Calculator


@pytest.fixture()
def cal():
    print("开始计算")
    cal = Calculator()
    yield cal
    print("计算结束")
