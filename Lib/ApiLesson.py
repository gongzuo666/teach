#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : ApiLesson.py
# Author: tian guang yuan
# Time  : 2020/6/20 21:03
from config import HOST
from Lib.ApiLogin import LoginClass
import requests,json
class LessonClass:
    # 1、新增接口
    def add_lesson(self, session, inData):
        user_cookie = {'sessionid': session}
        # 1、路径url
        api_url = f'{HOST}/api/mgr/sq_mgr/'
        header = {'Content-Type': 'application/x-www-form-urlencoded'}
        # 2、参数
        payload = {
            'action': 'add_course',
            'data': inData
        }
        reps = requests.post(api_url, data=payload, cookies=user_cookie)
        reps.encoding = 'unicode_escape'  # 设置响应编码--显示中文
        return reps.text  # 返回值可以自行定义
    # 2、列出接口
    def list_lesson(self,session,inData):
        user_cookie = {'sessionid': session}
        payload = inData
        # 1、路径-url
        api_url = f'{HOST}/api/mgr/sq_mgr/'
        reps = requests.get(api_url, params=payload, cookies=user_cookie)
        reps.encoding = 'unicode_escape'  # 设置响应编码--显示中文
        return reps.text

    # 3、删除课程
    def delete_all_lesson(self, session, inId):
        api_url = f'{HOST}/api/mgr/sq_mgr/'
        user_cookie = {'sessionid':session}
        header = {'Content-Type': 'application/x-www-form-urlencoded'}
        # 2、参数
        payload = {
            'action': 'delete_course',
            'id': inId
        }
        reps = requests.delete(api_url, data=payload,cookies=user_cookie)
        reps.encoding = 'unicode_escape'  # 设置响应编码--显示中文
        return reps.text

    def delete_lesson(self, session, inData):
        api_url = f'{HOST}/api/mgr/sq_mgr/'
        user_cookie = {'sessionid': session}
        payload = inData
        reps = requests.delete(api_url, data=payload,cookies=user_cookie)
        reps.encoding = 'unicode_escape'
        return reps.text
    # 4、修改课程
# 1、调试
# for i in range(1,3):
#     inData = {'action':'list_course',
#               'pagenum':i,
#               'pagesize':'20'
#             }
#     ss = LoginClass().login('{"username": "auto","password": "sdfsdfsdf"}')
#     res = json.loads(LessonClass().list_lesson(ss,inData))['retlist']
#     print(res)
#     for one in res:
#         print(one['id'])
#     LessonClass().list_lesson(ss,inData)
#     LessonClass().delete_lesson(ss,1503)

