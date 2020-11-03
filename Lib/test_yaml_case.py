#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : test_yaml_case.py
# Author: tian guang yuan
# Time  : 2020/7/5 15:59
import yaml
import pprint
# ------------------------读文件-----------------------
# # 操作yaml
# yamlDir = '../data/test.yaml'
# # 创建文件对象
# fo = open(yamlDir, 'r')
# # res = yaml.load(fo,Loader=yaml.FullLoader)
# # print(res)
#
# # 2、两组数据
# res = yaml.load_all(fo,Loader=yaml.FullLoader)
# for one in res:
#     print(one)

# ------------------------写文件-----------------------
# fo = open(yamlDir, 'a')
# data1 = {'name': 'tom', 'age': 20}
# data2 = [10,20,30,{'name': 'tom', 'age': 20}]
# # yaml.dump(data1, fo)  # 写一组数据
# yaml.dump_all([data1,data2],fo)  # 写多组数据
# fo.close()  # 关闭文件

# -------------------------登录-------------------
import json
def get_yaml_data():
    yamlDir = '../data/yaml_test.yaml'
    fo = open(yamlDir, 'r', encoding="utf8")
    res = yaml.load(fo, Loader=yaml.FullLoader)
    # pprint.pprint(res)
    # 封装数据
    resList = []
    for one in res:
        # print(json.dumps(one['data']), json.dumps(one['check'])).decode("unicode-escape")
        resList.append((json.dumps(one['data']), json.dumps(one['check']).encode('utf-8').decode('unicode_escape')))
    return resList

if __name__ == '__main__':
    print(get_yaml_data())














