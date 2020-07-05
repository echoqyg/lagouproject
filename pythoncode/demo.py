#!/usr/bin/env python
# encoding: utf-8

# print("test")
import fibo
import yaml

fibo.fib(1000)
fibo.fib3()
zoo = yaml.load(open("animail.yml"), Loader=yaml.FullLoader)
print(zoo["cat"])
