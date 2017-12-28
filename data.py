# -*- coding: utf8 -*-

import time

CurrentTime = time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))
Location = "Case&Result/"
CaseFileName = Location + "case.xlsx"
ResultFileName = Location + "Result_" + CurrentTime + ".xls"
SheetName = "Sheet1"

paramDoc = {
    # "bizid": "573ae98d7f10087a048b4a61",
    "from": "doctor_list"}


def select_env():
    print('请选择执行的环境：\n1:正式环境\n2:测试环境')
    env = int(raw_input())

    if env == 1:
        # 线上环境
        url_DocIndex = \
            "http://mobile.anxinyisheng.com/home/user/doc_detail"

        headers = {
            "Wxid": "oKoQnuEYYwxn7QbqKFIMiQJS-G_s",
            "Channel": "wx_anxinjiankang",
            "User-Agent": "micromessenger"}

        return [url_DocIndex, headers]

    elif env == 2:
        # 测试环境
        url_DocIndex = \
            "http://test.anxinyisheng.com/home/user/doc_detail"

        headers = {
            "Wxid": "o79aixECshqXft8Cck5fMC7LdYZs",
            "Channel": "wx_anxinjiankang",
            "User-Agent": "micromessenger"}

        return [url_DocIndex, headers]
