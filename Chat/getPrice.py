# -*- coding: utf8 -*-

import requests
import json
import xlrd
import xlwt
import Chat.dataOld as dataOld


# 记录请求结果，并保存
def get_price(name):
    data = dataOld.select_env()

    if data != 0:
        print ("\n*****************************\n测试开始，正在获取用例总数...")
        totalcase = dataOld.get_sum_case(data[2], data[3])
        print ("  用例总数为：%s\n    开始执行..." % totalcase)

        lenresult = len(get_result(data[0], get_param(data[2], 0), data[1]))
        matrix = [[0 for i in range(lenresult)] for i in range(totalcase)]

        for i in range(totalcase):
            print ("      正在执行caseId：%s" % (i + 1))
            matrix[i] = get_result(data[0], get_param(data[2], i), data[1])

        # print (matrix)

        print ("    执行完毕，开始保存结果...")
        w = xlwt.Workbook()
        ws = w.add_sheet(u'Sheet1')
        raw0 = ["docId", "docName", "hospitalName", "titleName", "hospitalLevel", "consultPrice", "qaPrice"]
        for i in range(len(raw0)):
            ws.write(0, i, raw0[i])

        for m in range(len(matrix)):
            for n in range(len(matrix[0])):
                ws.write(m + 1, n, matrix[m][n])

        w.save(name)
        print ("  保存成功，执行结束\n*****************************")

    else:
        return int(0)


# 请求接口，获取返回值
def get_result(host, params, header):
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


# 从case.xlsx获取dicid并填充至paramDoc
def get_param(filename, row):
    case = xlrd.open_workbook(filename)
    sheet = case.sheet_by_name("Sheet1")

    # 获取行数据
    while row < sheet.nrows:
        param = dict(_id=sheet.cell_value(row, 0))
        return param


get_price(dataOld.ResultFileName)
