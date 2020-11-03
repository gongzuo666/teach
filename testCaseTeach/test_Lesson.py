#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : test_Lesson.py
# Author: tian guang yuan
# Time  : 2020/6/20 21
from Lib.ApiLogin import LoginClass
from Lib.ApiLesson import LessonClass
import json,os
import pytest
import allure
'''
class TestLesson:# 测试用例类
    # 这个课程功能模块，每一个接口需要登录
    def setup_class(self):
        print('----登录模块------开始----')
        self.session = LoginClass().login('{"username": "auto","password": "sdfsdfsdf"}')
        print('----登录模块------结束----')
    # 1.新增课程接口
    @pytest.mark.lesson_add  # 标签--
    def test_add_lesson(self):
        inData = {"name":"田园123","desc":"初中化学课程","display_idx":"2"}
        print('----新增课程------开始----')
        res = LessonClass().add_lesson(self.session,inData)
        assert json.loads(res)['retcode'] == 0
        print('----新增课程------结束----')
    # 2.列出课程接口
    def test_list_lesson(self):
        print('----列出课程------开始----')
if __name__ == '__main__':
    pytest.main(['test_Lesson.py','-s','-m=lesson_add'])
'''
from Lib.GetExcelData import get_excelData


@allure.feature('课程模块')  # 一级标题
@pytest.mark.Lesson(order=2)  # 标签
class TestLesson:  # 测试用例类
    # 这个课程功能模块，每一个接口需要登录
    def setup_class(self):
        """课程模块——扥估初始化"""
        self.session = LoginClass().login('{"username": "auto","password": "sdfsdfsdf"}')
    # 1.新增课程接口
    @allure.severity("normal")
    @allure.story('新增课程')
    @allure.title('心增课程')
    @pytest.mark.lesson_add  # 标签--
    @pytest.mark.parametrize('inData,repsData',get_excelData('2-课程模块',2,26,6,8))
    def test_add_lesson(self,inData,repsData):
        print(inData)
        res = LessonClass().add_lesson(self.session,inData)
        assert json.loads(res)['retcode'] == json.loads(repsData)['retcode']
    # 2.列出课程接口
    @allure.severity("normal")
    @allure.story('列出课程')
    @allure.title('列出课程')
    @pytest.mark.lesson_list # 标签--
    @pytest.mark.parametrize('inData,repsData', get_excelData('2-课程模块',27,38,6,8))
    def test_list_lesson(self,inData,repsData):
        res = LessonClass().list_lesson(self.session,json.loads(inData))
        assert json.loads(res)['retcode'] == json.loads(repsData)['retcode']
    # 3.删除课程接口
    @allure.severity("normal")
    @allure.story('删除课程')
    @allure.title('删除课程')
    @pytest.mark.lesson_delete  # 标签--
    @pytest.mark.parametrize('inData,repsData', get_excelData('2-课程模块', 39, 46, 6, 8))
    def test_delete_lesson(self, inData, repsData):
        res = LessonClass().delete_lesson(self.session,json.loads(inData))
        assert json.loads(res)['retcode'] == json.loads(repsData)['retcode']

if __name__ == '__main__':
    pytest.main(['test_Lesson.py', '-sq'])

# if __name__ =="__main__":
#     # 执行pytest单元测试，生成 Allure 报告需要的数据存在 /tmp 目录
#     pytest.main(['test_lesson.py','-s','--alluredir', '../report/tmp'])
#     # 执行命令 allure generate ./tmp -o ./report --clean ，生成测试报告
#     os.system('allure generate  ../report/tmp -o ../report/report --clean')
