#!/usr/bin/env python
# -*- coding:utf-8 -*-


import requests
import json
import xlrd
import xlwt
import enc_selector

DOC_HOST = 'http://test.anxinyisheng.com'


def get_doc_header(mobile, pwd):  # 获取普通医生headers
    url_login = DOC_HOST + '/home/doctor/login'
    data = dict(mobile=mobile, password=pwd, mt='1532665210018', osType='Android', osVersion='5.1',
                imsi='867247022845142', imei='180723174342738', productID='Android-AnxinDoctor',
                productVersion='3.5.0.0706', packageName='com.hilficom.anxindoctor', mobileBrand='Meizu',
                mobileModel='MX5', screenHigh='1920', screenWidth='1080', netType='wifi', channel='hilficom')
    asp_login = requests.post(url=url_login, data=data).json()
    auth = asp_login['msg']['auth']
    header = {
        'Cookie': 'auth=' + auth
    }
    return header


def get_doc_info(mobile, pwd):
    url_me = DOC_HOST + '/home/doctor/me'
    header = get_doc_header(mobile, pwd)
    rsp = requests.post(url=url_me, headers=header).json()
    return [rsp["mobile"], rsp["_id"], rsp["name"], rsp["hospital"]["name"]]


def get_doc_price_list(mobile, pwd):
    url_price_list = DOC_HOST + 'xxxxxxxxx'  # 填写获取医生价格列表地址
    header = get_doc_header(mobile, pwd)
    rsp = requests.post(url=url_price_list, headers=header).json()
    return [rsp["msg"]["priceList"], rsp["msg"]["currentPrice"]]


def set_doc_chat_price(mobile, pwd, price):
    url_set_price = DOC_HOST + 'xxxxxxxxx'  # 填写提交医生价格地址
    header = get_doc_header(mobile, pwd)
    data = dict(price=price)
    requests.post(url=url_set_price, dada=data, headers=header).json()

