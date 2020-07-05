#!/usr/bin/env python
# encoding: utf-8
import pytest
import yaml

from pytest_homework_2.cal import Calculator


@pytest.fixture()
def cal():
    print("开始计算")
    cal = Calculator()
    yield cal
    print("计算结束")


def pytest_addoption(parser) -> None:
    mygroup = parser.getgroup("hogwarts")
    mygroup.addoption(
        "--env",
        default="test",
        dest="env",
        help="set your run env"
    )


@pytest.fixture(scope='session')
def cmdoption(request):
    myenv = request.config.getoption("--env", default='test')
    if myenv == 'test':
        print("获取测试数据")
        with open("datas/test/test.yml") as f:
            datas = yaml.safe_load(f)
    elif myenv == 'dev':
        print("获取dev数据")
        with open("datas/dev/dev.yml") as f:
            datas = yaml.safe_load(f)
    elif myenv == 'st':
        print("获取st数据")
        with open("datas/st/st.yml") as f:
            datas = yaml.safe_load(f)
    return datas
