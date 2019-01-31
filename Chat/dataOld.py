# -*- coding: utf8 -*-

import os
import time
import xlrd
import xlwt
import json
import requests


CurrentTime = time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))

Location = os.getcwd()
CaseTest = Location + "/CaseTest.xlsx"
CaseOnline = Location + "/CaseOnline.xlsx"
ResultFileName = Location + "/Result_" + CurrentTime + ".xls"

SheetName = "Sheet1"


def select_env():
    print('\n'
          '请输入数字选择执行环境\n'
          '1 -> 正式环境\n'
          '2 -> 测试环境\n')
    env = int(input(''))

    if env == 1:  # 线上正式环境
        print('\n已选择正式环境，即将开始执行...')
        host = "http://mobile.anxinyisheng.com/home/user/doc_detail"

        headers = {
            "Wxid": "oKoQnuEYYwxn7QbqKFIMiQJS-G_s",
            "Channel": "wx_anxinjiankang",
            "User-Agent": "micromessenger"}

        return [host, headers, CaseOnline, SheetName]

    elif env == 2:  # 测试环境
        print('\n已选择测试环境，即将开始执行...')
        host = "http://test.anxinyisheng.com/home/user/doc_detail"

        headers = {
            "Wxid": "o79aixECshqXft8Cck5fMC7LdYZs",
            "Channel": "wx_anxinjiankang",
            "User-Agent": "micromessenger"}

        return [host, headers, CaseTest, SheetName]


def get_sum_case(filename, sheet_name):  # 获得case.xlsx行数作为case总数
    workbook = xlrd.open_workbook(filename)
    sheet = workbook.sheet_by_name(sheet_name)
    return sheet.nrows


def get_price(name):  # 记录请求结果，并保存
    data = select_env()

    print("\n*****************************\n测试开始，正在获取用例总数...")
    total_case = get_sum_case(data[2], data[3])
    print("  用例总数为：%s\n    开始执行..." % total_case)

    len_result = len(get_result(data[0], get_param(data[2], 0), data[1]))
    matrix = [[0 for i in range(len_result)] for i in range(total_case)]

    for i in range(total_case - 1):
        print("      正在执行caseId：%s" % (i + 1))
        matrix[i] = get_result(data[0], get_param(data[2], i), data[1])

    # print (matrix)

    print("    执行完毕，开始保存结果...")
    w = xlwt.Workbook()
    ws = w.add_sheet(u'Sheet1')
    raw0 = ["docId", "docName", "hospitalName", "titleName", "hospitalLevel", "consultPrice", "qaPrice"]
    for i in range(len(raw0)):
        ws.write(0, i, raw0[i])

    for m in range(len(matrix)):
        for n in range(len(matrix[0])):
            ws.write(m + 1, n, matrix[m][n])

    w.save(name)
    print("  保存成功，执行结束\n*****************************")


def get_result(host, params, header):  # 请求接口，获取返回值
    url = host + '/home/user/doc_detail'
    rsp = requests.get(url=url, params=params, headers=header)
    rsp_json = json.loads(rsp.text)

    doc_id = rsp_json["msg"]["_id"]
    doc_name = rsp_json["msg"]["name"]
    hospital_name = rsp_json["msg"]["hospital"]["name"]
    title_name = rsp_json["msg"]["title"]["name"]
    hospital_level = rsp_json["msg"]["hospital"]["level"]
    consult_price = rsp_json["msg"]["priceList"]["consultationPrice"]
    qa_price = rsp_json["msg"]["priceList"]["qaPrice"]

    result = [doc_id, doc_name, hospital_name, title_name, hospital_level, consult_price, qa_price]
    print(result)

    return result


def get_param(filename, row): # 从case.xlsx获取dicId并填充至param
    case = xlrd.open_workbook(filename)
    sheet = case.sheet_by_name("Sheet1")

    # 获取行数据
    while row < sheet.nrows:
        return dict(_id=sheet.cell_value(row, 0))


get_price(ResultFileName)
