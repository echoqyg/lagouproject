#!/usr/bin/env python
# encoding: utf-8
import yaml

print(
    yaml.safe_load(open("./data.yml"))["add"]
)
print(
    yaml.safe_load(open("./data.yml"))["sub"]
)
print(
    yaml.safe_load(open("./data.yml"))["mul"]
)
print(
    yaml.safe_load(open("./data.yml"))["div"]
)
