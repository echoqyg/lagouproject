#!/usr/bin/env python
# encoding: utf-8
import pytest
import yaml


class Checkdemo1:

    @pytest.mark.parametrize('a,b,result', yaml.safe_load(open("./data.yml"))["add"])
    def check_add(self, a, b, result, cal):
        assert result == cal.add(a, b)
