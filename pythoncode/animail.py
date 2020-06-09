#!/usr/bin/env python
# encoding: utf-8
import yaml


class Animal:
    name = ""
    color = ""
    age = ""
    gender = ""

    def __init__(self, name, color, age, gender):
        self.name = name
        self.color = color
        self.age = age
        self.gender = gender

    def call(self):
        print("会叫")

    def run(self):
        print("会跑")


class cat(Animal):
    hair = ""

    def __init__(self, kwargs):
        self.name = kwargs["name"]
        self.color = kwargs["color"]
        self.age = kwargs["age"]
        self.gender = kwargs["gender"]
        self.hair = kwargs["hair"]

    def call(self):
        print(f"{self.name}会喵喵叫")

    def ability(self):
        print(f"猫猫叫{self.name}, 颜色是{self.color}，年龄是{self.age}，性别是{self.gender}，毛发为{self.hair}, 捉到了老鼠")


class dog(Animal):
    hair = ""

    def __init__(self, kwargs):
        self.name = kwargs["name"]
        self.color = kwargs["color"]
        self.age = kwargs["age"]
        self.gender = kwargs["gender"]
        self.hair = kwargs["hair"]

    def call(self):
        print(f"{self.name}会汪汪叫")

    def ability(self):
        print(f"狗狗叫{self.name}, 颜色是{self.color}，年龄是{self.age}，性别是{self.gender}，毛发为{self.hair}")
        print(f"{self.name}会看家")


# a = cat("红", "白色", "3岁", "母")
# a.ability()
# a.call()
# b = dog("黑", "白色", "3岁", "母")
# b.ability()
# b.call()

""" 
打印内容为
猫猫叫红, 颜色是白色，年龄是3岁，性别是母，毛发为短毛, 捉到了老鼠
红会喵喵叫
狗狗叫黑, 颜色是白色，年龄是3岁，性别是母，毛发为长毛
黑会看家
黑会汪汪叫
"""

zoo = yaml.load(open("animail.yml"), Loader=yaml.FullLoader)
a = cat(zoo["cat"])
a.ability()
a.call()
b = dog(zoo["dog"])
b.ability()
b.call()
