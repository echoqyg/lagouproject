#!/usr/bin/env python
# encoding: utf-8
from api.base_api import BaseApi


class TagApi(BaseApi):
    def test_create(self, tagname, tagid, token):
        # https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token=ACCESS_TOKEN
        """
        :param tagname: 标签名称，长度限制为32个字以内（汉字或英文字母），标签名不可与其他标签重名
        # :param tagid:(可以不指定) 标签id，非负整型，指定此参数时新增的标签会生成对应的标签id，不指定时则以目前最大的id自增。
        :param token:调用接口凭证
        :return:"errmsg": "created"
        """
        data = {
            "method": "post",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token={token}",
            "json": {
                "tagname": tagname,
                "tagid": tagid
            }
        }
        res = self.send_api(data)
        return res

    def test_update(self, tagname, tagid, token):
        """

        :param tagname:
        :param tagid:标签ID
        :param token:标签名称，长度限制为32个字（汉字或英文字母），标签不可与其他标签重名。
        :return:  "errmsg": "updated"
        """
        # https://qyapi.weixin.qq.com/cgi-bin/tag/update?access_token=ACCESS_TOKEN
        data = {
            "method": "post",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/tag/update?access_token={token}",
            "json": {
                "tagname": tagname,
                "tagid": tagid
            }
        }
        res = self.send_api(data)
        return res

    def test_delete(self, tagid, token):
        # "errmsg": "deleted"
        # https://qyapi.weixin.qq.com/cgi-bin/tag/delete?access_token=ACCESS_TOKEN&tagid=TAGID
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/tag/delete",
            "params": {
                "access_token": token,
                "tagid": tagid
            }
        }
        res = self.send_api(data)
        return res

    def test_getlist(self, token):
        # "errmsg": "ok",
        # "taglist": [
        #     {"tagid": 1, "tagname": "a"},
        #     {"tagid": 2, "tagname": "b"}
        # ]
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/tag/list",
            "params": {
                "access_token": token
            }
        }
        res = self.send_api(data)
        return res
