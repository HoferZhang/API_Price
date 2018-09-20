#!/usr/bin/env python
# -*- coding:utf-8 -*-


import requests
import xlrd
import xlwt
import time


CurrentTime = time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))
Location = "Case&Result/"
CaseFileName = Location + "case_ChatPriceSelf.xlsx"
ResultFileName = Location + "Result_ChatPriceSelf_" + CurrentTime + ".xls"

ONLINE_HOST = "http://mobile.anxinyisheng.com"
ONLINE_WX_HEADER = {
            "Wxid": "oKoQnuEYYwxn7QbqKFIMiQJS-G_s",
            "Channel": "wx_anxinjiankang",
            "User-Agent": "micromessenger"}

TEST_HOST = "http://test.anxinyisheng.com"
TEST_WX_HEADRER = {
            "Wxid": "o79aixBGu8V6uCzBDVlbsNOeTsPA",
            "Channel": "wx_anxinjiankang",
            "User-Agent": "micromessenger"}


def run_entrance():
    info = select_env()
    host = info[0]
    wx_header = info[1]

    print("\n*****************************\n测试开始，正在获取用例总数...")
    totalcase = get_sum_case(CaseFileName, 'Sheet1')
    print("  用例总数为：%s\n    开始执行..." % totalcase)

    lenresult = len(chat_price(host, wx_header, read_case(CaseFileName, 1)[0], read_case(CaseFileName, 1)[1]))
    matrix = [[0 for i in range(lenresult)] for i in range(totalcase)]
    # print(matrix)

    for i in range(totalcase):
        print("      正在执行caseId：%s" % (i + 1))
        matrix[i] = chat_price(host, wx_header, read_case(CaseFileName, i)[0], read_case(CaseFileName, i)[1])
    # print(matrix)

    print("    执行完毕，开始保存结果...")
    w = xlwt.Workbook()
    ws = w.add_sheet(u'Sheet1')
    raw0 = ["mobile", "docid", "docName", "hospital", "priceList", "currentPrice", "setPrice", "wxPrice"]
    for i in range(len(raw0)):
        ws.write(0, i, raw0[i])

    for m in range(len(matrix)):
        for n in range(len(matrix[0])):
            ws.write(m + 1, n, matrix[m][n])

    w.save(ResultFileName)
    print("  保存成功，执行结束\n*****************************")


def chat_price(host, wx_header, mobile, price, pwd=123456):

    # 获取headers
    url_login = host + '/home/doctor/login'
    data = dict(mobile=mobile, password=pwd, mt='1532665210018', osType='Android', osVersion='5.1',
                imsi='867247022845142', imei='180723174342738', productID='Android-AnxinDoctor',
                productVersion='3.5.0.0706', packageName='com.hilficom.anxindoctor', mobileBrand='Meizu',
                mobileModel='MX5', screenHigh='1920', screenWidth='1080', netType='wifi', channel='hilficom')
    asp_login = requests.post(url=url_login, data=data).json()
    if int(asp_login["code"]) == 200:
        auth = asp_login['msg']['auth']
        header = {'Cookie': 'auth=' + auth}
    else:
        chat_price(host, price, mobile, pwd=111111)

    # 获取医生信息
    url_me = host + '/home/doctor/me'
    rsp_me = requests.post(url=url_me, headers=header).json()
    # print(rsp_me)
    info = [rsp_me["msg"]["mobile"], rsp_me["msg"]["_id"], rsp_me["msg"]["name"], rsp_me["msg"]["hospital"]["name"]]

    # 获取医生可配置收入列表
    url_price_list = host + '/home/chat/getDocChatPriceOptions'  # 获取医生价格列表地址
    rsp_price_list = requests.post(url=url_price_list, headers=header).json()
    a_list = rsp_price_list["msg"]["priceList"]
    s_list = ''
    for i in a_list:
        s_list = s_list + str(i) + ","
    price_list = [s_list, str(rsp_price_list["msg"]["currentPrice"]), str(price)]

    # 医生提交自主定价
    url_set_price = host + '/home/chat/docSetChatPriceConf'  # 填写提交医生价格地址
    data = dict(price=price)
    requests.post(url=url_set_price, data=data, headers=header).json()

    # 患者端获取医生在线咨询服务价格
    url_wx_doc_main = host + '/home/user/doc_detail'
    params =dict(_id=rsp_me["msg"]["_id"], bizid=rsp_me["msg"]["_id"])
    rsp_wx_doc_main = requests.get(url=url_wx_doc_main, params=params, headers=wx_header).json()
    price_wx = [str(rsp_wx_doc_main["msg"]["priceList"]["consultationPrice"])]

    result = info + price_list + price_wx
    # print(result)
    return result


# 选择执行环境
def select_env():
    print('\n'
          '请输入[数字]选择执行环境\n'
          '1 -> 正式环境\n'
          '2 -> 测试环境\n')
    host = int(input(''))

    if host == 1:  # 线上正式环境
        print('\n已选择正式环境，即将开始执行...')
        return [ONLINE_HOST, ONLINE_WX_HEADER]
    elif host == 2:  # 测试环境
        print('\n已选择测试环境，即将开始执行...')
        return [TEST_HOST, TEST_WX_HEADRER]
    else:
        print('\n输入错误，请重新输入...')
        select_env()


# 获得case文件行数作为用例总数
def get_sum_case(filename, sheetname):
    workbook = xlrd.open_workbook(filename)
    sheet = workbook.sheet_by_name(sheetname)
    return sheet.nrows


# 读取所有case内容
def read_case(filename, row):
    case = xlrd.open_workbook(filename)
    sheet = case.sheet_by_name("Sheet1")

    # 获取行数据
    a = []
    if row < sheet.nrows:
        for i in range(len(sheet.row_values(row))):
            a.append(int(sheet.cell_value(row, i)))
    return a

run_entrance()