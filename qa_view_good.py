# -*- coding: utf8 -*-

import requests


wxid_list = ["o79aixBGu8V6uCzBDVlbsNOeTsPA", "o79aixBGu8V6uCzBDVlbsNOeTsPA"]
header = {
        'Wxid': "",
        'Channel': "wx_anxinjiankang",
        'User-Agent': "micromessenger"
    }


def get_question_form_qaMain(pageSize):
    url = "http://test.anxinyisheng.com/home/question/getIndexStream"
    params = {
        "catalog": 1,
        "pageIndex": 1,
        "pageSize": pageSize
    }

    a = []
    rsp = requests.get(url=url, params=params, headers=header).json()
    q_list = rsp["msg"]["lists"]
    for i in q_list:
        a.append(i["questionId"])
    return a


def view_q(qid):
    url = "http://test.anxinyisheng.com/home/question/detailQuestion"
    params = {
        "questionId": qid
    }
    rsp = requests.get(url=url, params=params, headers=header).json()
    if rsp["desc"] == "成功":
        print(qid + "查看成功")


def raise_q(qid):
    url = "http://test.anxinyisheng.com/home/question/raise"
    params = {
        "questionId": qid
    }
    rsp = requests.get(url=url, params=params, headers=header).json()
    if rsp["desc"] == "成功":
        print(qid + "点赞成功")


def run():
    qid_list = get_question_form_qaMain(100)
    for i in wxid_list:
        for k in qid_list:
            header["Wxid"] = i
            view_q(k)
            raise_q(k)


run()
