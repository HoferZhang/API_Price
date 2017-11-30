# -*- coding: utf8 -*-

import requests
import json
import xlrd
import xlwt


CaseFileName = "case.xlsx"
ResultFileName = "result.xls"
SheetName = "Sheet1"

url_DocIndex = \
    "http://test.anxinyisheng.com/home/user/doc_detail"

paramDoc = {
    "bizid": "573ae98d7f10087a048b4a61",
    "from": "doctor_list"}

headers = {
    "Wxid": "o79aixECshqXft8Cck5fMC7LdYZs",
    "Channel": "wx_anxinjiankang",
    "User-Agent": "micromessenger"}


# 执行请求，保存结果
def run(name):
    print ("***测试开始，获取用例数***")
    totalcase = get_sum_case(CaseFileName, SheetName)
    print ("***用例总数为：%s***"%totalcase)
    lenresult = len(get_result(url_DocIndex, get_param(paramDoc, CaseFileName, 0), headers))
    matrix = [[0 for i in range(lenresult)] for i in range(totalcase)]

    for i in range(totalcase):
        print ("正在执行caseId：%s"%i)
        matrix[i] = get_result(url_DocIndex, get_param(paramDoc, CaseFileName, i), headers)

    # print (matrix)

    print ("***执行完毕，开始保存结果***")
    w = xlwt.Workbook()
    ws = w.add_sheet(u'Sheet1')

    for m in range(len(matrix)):
        for n in range(len(matrix[0])):
            ws.write(m, n, matrix[m][n])

    w.save(name)
    print ("***保存成功，执行结束***")


# 请求接口，获取结果
def get_result(url, params, header):
    rsp = requests.get(url=url, params=params, headers=header)
    rsp_json = json.loads(rsp.text)

    doc_id = rsp_json["msg"]["_id"]
    doc_name = rsp_json["msg"]["name"]
    hospital_name = rsp_json["msg"]["hospital"]["name"]
    hospital_level = rsp_json["msg"]["hospital"]["level"]
    consult_price = rsp_json["msg"]["priceList"]["consultationPrice"]
    qa_price = rsp_json["msg"]["priceList"]["qaPrice"]

    result = [doc_id, doc_name, hospital_name, hospital_level, consult_price, qa_price]

    return result


def get_param(param, filename, row):
    case = xlrd.open_workbook(filename)
    sheet = case.sheet_by_name("Sheet1")

    # 获取行数据
    while row < sheet.nrows:
        param["_id"] = sheet.cell_value(row, 0)
        return param
    else:
        return 0


def get_sum_case(filename, sheetname):
    workbook = xlrd.open_workbook(filename)
    sheet = workbook.sheet_by_name(sheetname)

    return sheet.nrows


run(ResultFileName)
