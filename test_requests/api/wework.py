#!/usr/bin/env python
# encoding: utf-8
from api.base_api import BaseApi


class WeWork(BaseApi):
    def test_get_token(self):
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params": {
                "corpid": "wwaabe2ad82255f238",
                "corpsecret": "gRI4K5pjUX2R34YSKeK2CkMcvtluBO3OUQlWQaNPfNk"
            }
        }
        res = self.send_api(data)
        try:
            return res['access_token']
        except Exception as e:
            raise ValueError("requests token error")
