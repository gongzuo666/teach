#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : GetTxtData.py
# Author: tian guang yuan
# Time  : 2020/6/23 22:22
import xlrd
import pprint


def get_excelData(sheetName, startRow, endRow, bodyCol, repsCol):
    # 文件路径
    excelDir = '../data/松勤-教管系统接口测试用例-v1.4.xls'
    # 打开excels
    workBook = xlrd.open_workbook(excelDir, formatting_info=True)  # 保存原样 -- 样式
    # 操作对应的用例表
    workSheet = workBook.sheet_by_name(sheetName)  # 通过表名获取
    dataList = []
    for cut in range(startRow-1, endRow):
        cellData = workSheet.cell_value(cut, bodyCol)  # 字符串类型
        repsCellData = workSheet.cell_value(cut, repsCol)
        dataList.append((cellData, repsCellData))
    return dataList  # 列表


if __name__ == '__main__':
    print(get_excelData('1-登录接口', 2, 5, 6, 8))
'''
:param sheetName: 表名
:param startRow: 开始行数
:param endRow: 结束函数
:param bodyCol: 请求体列数
:param repsCol: 响应体列数
:return: [(请求体，响应体),(请求体，响应体)]
'''
# import json
# def get_excelData():
#     # 文件路径
#     excelDir = r'E:\songqin\teach\data\松勤-教管系统接口测试用例-v1.4.xls'
#     # 打开excelr
#     workBook = xlrd.open_workbook(excelDir, formatting_info=True)  # 保存原样 -- 样式
#     # 操作对应的用例表
#     workSheet = workBook.sheet_by_name('2-课程模块')  # 通过表名获取
#     dataList = []
#     for cut in range(1,2):
#       cellData = workSheet.cell_value(cut,6)  # 字符串类型
#       repsCellData = workSheet.cell_value(cut, 8)
#       dataList.append((cellData,repsCellData))
#     # return dataList  # 列表
#     # print(dataList)
#     pprint.pprint(dataList)
#
# if __name__ == '__main__':
#     print(get_excelData())
