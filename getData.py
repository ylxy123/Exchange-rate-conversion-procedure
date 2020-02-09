# @Time : 2020/2/6 16:42
# @Author : YLXY
# @File : getData.py
# -*- coding: utf-8 -*-

import requests
import csv

# 常用货币汇率数据
def getdata(url):
    r = requests.get(url)
    response_dict = r.json()
    data = response_dict['result']['list']
    with open('database.csv', 'w',encoding='utf-8') as f:
        csv_f = csv.writer(f)
        csv_f.writerow(['货币名称','交易单位','现汇买入价','现钞买入价','现钞卖出价','中行折算价'])
        for i in data:
            csv_f.writerow(i)
    for i in range(len(data)):
        print(data[i])

# 货币缩写查询
def getmoneyname(money):
    with open('moneylist.txt', 'r', encoding='utf-8') as f:
        content = f.readlines()
        money_dict = ''
        for line in content:
            money_dict += line.strip('\n').strip(' ')
        money_dict = eval(money_dict)
    return money_dict[money]


# 实时汇率查询转换
def cur_exchange(appkey, former, new):
    url = 'http://op.juhe.cn/onebox/exchange/currency'
    r = requests.get(url+'?key='+appkey+'&from='+former+'&to='+new)
    response_dict = r.json()

    if response_dict:
        error_code = response_dict['error_code']
        if error_code == 0:
            # 请求成功
            return "1:" + response_dict['result'][0]['result']
        else:
            print("%s：%s" %(response_dict['error_code'], response_dict['reason']))
    else:
        print("appkey错误")


