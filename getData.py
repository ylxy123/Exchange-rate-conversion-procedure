# @Time : 2020/2/6 16:42
# @Author : YLXY
# @File : getData.py
# -*- coding: utf-8 -*-

import requests
import csv

# 获取数据

def getdata(url):
    r = requests.get(url)
    response_dict = r.json()
    data = response_dict['result']['list']
    with open('database.csv', 'w',encoding='utf-8') as f:
        csv_f = csv.writer(f)
        csv_f.writerow(['货币名称','交易单位','现汇买入','现钞买入价','现钞卖出价','中行折算价'])
        for i in data:
            csv_f.writerow(i)
    for i in range(len(data)):
        print(data[i])

if __name__ == "__main__":
    getdata('http://op.juhe.cn/onebox/exchange/query?key=cd0ddf0d24e0291f18d0d519d04700af')
