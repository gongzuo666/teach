#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : test_login.py
# Author: tian guang yuan
# Time  : 2020/6/20 21:37
from Lib.ApiLogin import LoginClass
import pytest
import json
import allure
from Lib.GetExcelData import get_excelData
from Lib.test_yaml_case import get_yaml_data
'''
def test_login():
   res = LoginClass().login('auto', 'sdfsdfsdf')[1]
   assert json.loads(res)['retcode'] == 0


if __name__ == '__main__':
   pytest.main(['test_login.py','-s'])
'''


# def get_excelData():
#     # 文件路径
#     excelDir = r'C:\Users\Administrator\Desktop\松勤-教管系统接口测试用例-v1.4.xls'
#     # 打开excel
#     workBook = xlrd.open_workbook(excelDir, formatting_info=True)  # 保存原样 -- 样式
#     # 操作对应的用例表
#     workSheet = workBook.sheet_by_name('1_登录接口')  # 通过表名获取
#     dataList = []
#     for cut in range(1, 5):
#         cellData = workSheet.cell_value(cut, 6)  # 字符串类型
#         repsCellData = workSheet.cell_value(cut, 8)
#         dataList.append((cellData, repsCellData))
#     return dataList  # 列表

@allure.feature('登录模块')
@allure.story('登录接口')
@allure.title('登录接口用例')
@allure.severity("critical")
@pytest.mark.parametrize('inData,repsData', get_yaml_data())
def test_login(inData, repsData):
    res = LoginClass().login(inData, getSession=False)
    assert json.loads(res)['retcode'] == json.loads(repsData)['retcode']  # 断言

@allure.severity("critical")
@allure.story("登录界面")
@allure.description("这里只是做一个web ui自动化的截图效果")
def test_login_image():
    allure.attach.file(r'../data/test.jpg', '我是附件截图的名字',
                           attachment_type=allure.attachment_type.JPG)

if __name__ == '__main__':
    pytest.main(['test_login.py', '-sq'])
