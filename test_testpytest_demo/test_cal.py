#!/usr/bin/env python
# encoding: utf-8
# !/usr/bin/env python
# encoding: utf-8
import pytest
import yaml


class Test_cal:

    @pytest.mark.parametrize('a,b,result', yaml.safe_load(open("./data.yml"))["add"])
    def test_add(self, a, b, result, cal):
        assert result == cal.add(a, b)

    @pytest.mark.parametrize('a,b,result', yaml.safe_load(open("./data.yml"))["sub"])
    def test_sub(self, a, b, result, cal):
        assert result == cal.sub(a, b)

    @pytest.mark.parametrize('a,b,result', yaml.safe_load(open("./data.yml"))["mul"])
    def test_mul(self, a, b, result, cal):
        assert result == cal.mul(a, b)

    @pytest.mark.parametrize('a,b,result', yaml.safe_load(open("./data.yml"))["div"])
    def test_div(self, a, b, result, cal):
        assert result == cal.div(a, b)
