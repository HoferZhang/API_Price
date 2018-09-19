# -*- coding: utf8 -*-

import time
import xlrd

CurrentTime = time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))
Location = "Case&Result/"
CaseFileName = Location + "case.xlsx"
ResultFileName = Location + "Result_" + CurrentTime + ".xls"
SheetName = "Sheet1"

paramDoc = {
    # "bizid": "573ae98d7f10087a048b4a61",
    "from": "doctor_list"}


def select_env():
    print('\n'
          '请输入数字选择执行环境\n'
          '1 -> 正式环境\n'
          '2 -> 测试环境\n')
    env = int(input(''))

    if env == 1:
        # 线上正式环境
        print('\n已选择正式环境，即将开始执行...')
        url_DocIndex = \
            "http://mobile.anxinyisheng.com/home/user/doc_detail"

        headers = {
            "Wxid": "oKoQnuEYYwxn7QbqKFIMiQJS-G_s",
            "Channel": "wx_anxinjiankang",
            "User-Agent": "micromessenger"}

        return [url_DocIndex, headers]

    elif env == 2:
        # 测试环境
        print('\n已选择测试环境，即将开始执行...')
        url_DocIndex = \
            "http://test.anxinyisheng.com/home/user/doc_detail"

        headers = {
            "Wxid": "o79aixECshqXft8Cck5fMC7LdYZs",
            "Channel": "wx_anxinjiankang",
            "User-Agent": "micromessenger"}

        return [url_DocIndex, headers]
    else:
        return 0



# 获得case.xlsx行数作为case总数
def get_sum_case(filename, sheetname):
    workbook = xlrd.open_workbook(filename)
    sheet = workbook.sheet_by_name(sheetname)

    return sheet.nrows