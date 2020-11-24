#!/usr/bin/env python
# encoding: utf-8
import json

import requests


class TestWeworkAccess:

    def set_r(self):
        params = {
            "access_token": self.test_get_token()
        }
        r = requests.Session()
        r.params = params
        return r

    def test_get_token(self):
        params = {
            "corpid": "",
            "corpsecret": ""
        }
        res = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/gettoken", params=params)
        try:
            token = res.json()['access_token']
            print(res.json())
            return token
        except Exception as e:
            raise ValueError("requests token error")

    def test_add(self):
        r = self.set_r()
        data = {
            "userid": "zhangsan",
            "name": "张三",
            "mobile": "+86 13800000000",
            "department": [1]
        }
        res = r.post("https://qyapi.weixin.qq.com/cgi-bin/user/create",
                     json=data)
        print(res.json())

    def test_get(self):
        r = self.set_r()
        r.params["userid"] = "zhangsan"
        res = r.get("https://qyapi.weixin.qq.com/cgi-bin/user/get")
        print(res.json())

    def test_update(self):
        r = self.set_r()
        data = {
            "userid": "zhangsan",
            "name": "李四",
            "department": [1],
            "order": [10],
            "position": "后台工程师",
            "mobile": "13800000000"
        }
        res = requests.post("https://qyapi.weixin.qq.com/cgi-bin/user/update", json=data)

    def test_delete(self):
        r = self.set_r()
        r.params["userid"] = "zhangsan"
        res = r.get("https://qyapi.weixin.qq.com/cgi-bin/user/delete")
        print(res.json())
