#!/usr/bin/env python
# encoding: utf-8
import requests


class BaseApi:
    def send_api(self, req):
        # 请求的封装
        return requests.request(**req).json()
