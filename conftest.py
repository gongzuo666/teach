#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : conftest.py
# Author: tian guang yuan
# Time  : 2020/6/21 21:54
import pytest
import json
from Lib.ApiLogin import LoginClass
from Lib.ApiLesson import LessonClass


@pytest.fixture(scope='module', autouse=True)  # 环境初始化，数据清除
def delete_all_lesson(request):
    print('-------------------开始-------------------')
    # 1、登录
    session = LoginClass().login('{"username": "auto","password": "sdfsdfsdf"}')
    # 2、列出所有课程
    inData = {'action': 'list_course',
              'pagenum': 1,
              'pagesize': '20'
              }
    resList = json.loads(LessonClass().list_lesson(session, inData))['retlist']
    while resList != []:
        for one in resList:
            lessonId = one['id']  # 获取课程id
            # 3、删除所有的课程
            LessonClass().delete_all_lesson(session, lessonId)
        resList = json.loads(LessonClass().list_lesson(session, inData))['retlist']
    print('---------------------结束-------------------')

    # # 增加课程测试数据
    # for one in range(1,15):
    #     lessonData =  {"name":f"田园{one:0>3}","desc":"初中化学课程","display_idx":f"{one}"}
    #     LessonClass().add_lesson(session,lessonData)
    # 环境 数据清除-----teardown
    def fin():
        print('-----------测试数据恢复-------------')
        inData = {'action': 'list_course',
                  'pagenum': 1,
                  'pagesize': '20'
                  }
        resList = json.loads(LessonClass().list_lesson(session, inData))['retlist']
        while resList != []:
            for one in resList:
                lessonId = one['id']  # 获取课程id
                # 3、删除所有的课程
                LessonClass().delete_all_lesson(session, lessonId)
            resList = json.loads(LessonClass().list_lesson(session, inData))['retlist']

    request.addfinalizer(fin)
