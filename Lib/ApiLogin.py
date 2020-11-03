#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : ApiLogin.py
# Author: tian guang yuan
# Time  : 2020/6/20 20:57
import requests
from config import HOST
import json
'''
class LoginClass:
    def login(self,username,password):
        # 1、路径-url
        log_url = f'{HOST}/api/mgr/loginReq'
        header = {'Content-Type': 'application/x-www-form-urlencoded'}
        # 2、参数
        payload = {"username": username,'password': password}
        reps = requests.post(log_url, data=payload, headers=header)
        reps.encoding = 'unicode_escape'  # 设置响应编码--显示中文
        return reps.cookies['sessionid'],reps.text

if __name__ == '__main__':
   print(LoginClass().login('auto','sdfsdfsdf'))
'''
class LoginClass:
    def login(self,indata,getSession = True):
        """

        :rtype: object
        """
        # 1、路径-url
        log_url = f'{HOST}/api/mgr/loginReq'
        header = {'Content-Type': 'application/x-www-form-urlencoded'}
        # 2、参数
        payload = json.loads(indata)
        # print(payload)
        reps = requests.post(log_url, data=payload, headers=header)
        reps.encoding = 'unicode_escape'  # 设置响应编码--显示中文
        if getSession:
            return reps.cookies['sessionid']
        else:
            return reps.text

if __name__ == '__main__':
    print(LoginClass().login('{"username": "auto","password": "sdfsdfsdf"}'))
