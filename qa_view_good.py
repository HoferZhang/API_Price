# -*- coding: utf8 -*-

import requests


wxid_list = [
    "o79aixHf4cFEuY2lnBwDOiNi9qjA", "o79aixMA08dXfA2WrstHHAOGgRcE", "o79aixPoRGSNPJPnmJ9b0eBtgyZ8",
    "o79aixDNk4BtsVVNk_sVlOw3FFA8", "o79aixHM1jaFx9H3zVLdPfoUAAjo", "o79aixPFHiKbzzYLE6rog7j_2pwc",
    "o79aixJKoxo5odYSNfIjq8bslA_E", "o79aixGJDntefIDEucWJL71UFWbQ", "o79aixNouUo3CbZGOcUEnCbPtkHw",
    "o79aixAJuXDGpngdVll-6hVsAqx0", "ok8UpwhorEJ_Gh4ebHlAQdLEvtJQ", "o79aixODDV-LhUPD0nbjwzvDDp9E",
    "o79aixN4l-jV7Z7JOIMy6aeo5Ihw", "o79aixMc_f1A8Nm4fBK2c1uYIjWQ", "o79aixECshqXft8Cck5fMC7LdYZs",
    "o79aixJfmD3XSJiT8isQVVznrHQY", "ok8UpwrNqq0T6mheE_9mRa_-4SMM", "o79aixNGqrzH9seQTzXyk2ENVTrc",
    "o79aixObbhtdoU8fCUdAZ7DGg_10", "o79aixHnOJravrWh2SXwPlzmEvWg", "o79aixEQuJdSa6UtpKqBGrFRxyMw",
    "o79aixBj5eh1FmLPYY3_TJaiSt0Y", "o79aixPQaLB6KcKHH-vrnZlysSlI", "o79aixCOkFr5rEVTKHcEIr2VYXCo",
    "o79aixE4svscOP17UD-inQ6Yywqo", "o79aixJlPHdEKMxulXzCmzv2e3yY", "o79aixJrdpNIxo2tsOCus8XcYeY4",
    "o79aixISOt0rZWZ5a9PwuPusVXKY", "o79aixG4iJ3E-YgDNBPQdiw4cG68", "o79aixJWxFOCesOsFYiOPGRRKiT8",
    "o79aixBFO_t2y-hoTG1I0hNquito", "o79aixCGok9KE1QBGaAVkD4VB3E4", "o79aixHXBG9KAh4s7d9YZRLfSapQ",
    "o79aixPHbSLJlXc9YOdidLkOJGWU", "o79aixJePQW-pxATGthGRlfKp4P4", "o79aixC0rr0lxistBxTgzwuQziv8",
    "o79aixLe47BnDtKelEj38mRaZ4GI1478254122", "o79aixLe47BnDtKelEj38mRaZ4GI", "o79aixM0AAodWa1-WAIxw01Wd2MY",
    "o79aixPpQtVQ92KCfIyYnrL4Nleg", "o79aixOmZ-ZYvEFoRTCCYkFv01HY", "o79aixEAN1hYqRTI49hmgttFsjyU",
    "o79aixNS1et2ti-H8Ga0abnOb3TU", "o79aixFjrI_HmffGGP0driKh0Oi8", "o79aixPWUj-Ig7yd2O9jS9-DqWL0",
    "o79aixKOhhYHefL6FsgiHOh7If2Y", "o79aixM3h6QYI6ZmVtcUO070mIMU", "o79aixMHAlBh26aR4aKhGGQETDX8",
    "o79aixFP9oRteud2kc4kV5mt8wR0", "o79aixK6xsD2Apl1SaQmQbbtTRYI", "o79aixHXjSQ2gMywv3KwTkFBZWnQ",
    "o79aixAH7U1tYK9aaZgTcYpf30XQ", "o79aixIYfY8kwWRPdT2B5vNmw6wQ", "o79aixG7II7UNZt9h4SSbYhJ7_u8_00",
    "o79aixKru-4wYAdb84jt_9nDcbQk", "o79aixEtmskl6eqd0ZriQTimHn6o", "o79aixAiXF6ijAKVk1Wtt5Eckghw",
    "o79aixAjbc2zGsOLzZjkqu2ogOpU", "oKoQnuJ2oVS2SxD-G6fEc1q9fuOY", "o79aixNF6EpNnMvsQWo10xQ34jSo",
    "o79aixBtCyDOG-ROz32rfKNMd7ig", "o79aixOXBJ5kS1lZnv56ploG2bBI", "o79aixKK0qJQ4ItemgXLQk6dYj-c",
    "o79aixHJPOx0EYHDF8mfZi1LNMl4", "ok8UpwsmOgz2tdbSCd4aLsI6CeIM", "o79aixMYDUHVrrC9gtMugOYU-Rzg",
    "o79aixNkPlzfkbo1J-Q3-TC8vvHg", "o79aixFO-xsK4yPyuZ443bjQX7KU", "o79aixMl1A7nr-LqSBk1J0MneLuI",
    "o79aixLbrLKCyaj5whxXLPCZzOIY", "oKoQnuCKNp5r26ghgh52cgmrpuvM", "o79aixGX2gxz1RAQeIH-5pY1rfMQ",
    "o79aixPRFgx4PNQcTq-LUMbo38D4", "ok8UpwuqwvOnX-8ihLPL9psP6UZ8", "o79aixIgLqmTECNHS8nfEH7Pe7hg",
    "o79aixPngbmogH-c1oU1_2BBr5kw1468469256", "o79aixPngbmogH-c1oU1_2BBr5kw", "o79aixLDk7tIGzNu1941WXdeyg78",
    "o79aixORWJjYoZ7_SzLhJNrkbnMg", "o79aixMJOVkaTmED19M8Mw7_Wl0s", "o79aixIh16CjklXAiBfafG-HQVzI",
    "ok8UpwvwRd3OD1G_Fhxr-yszhSik", "o79aixMXrpAOxRCeyBc_t-mZNXvE", "o79aixE-G_MIuE2uKp_QYBklQRj4",
    "oKoQnuL-slzKxyLbk_1atP4o8kG8", "o79aixKxc3WuoUCFVfqf0_z4MGhQ", "o79aixGONyn9X8xPyZmDjAC0eWXQ",
    "ok8UpwnZlEuNb1BAG70UPL-kLzg4", "ok8UpwrSv2n8ki9DkbMTV_o8bZIo", "o79aixACKO8DxCSl4oDmm5Ka6dgE",
    "o79aixGTRO2fjPcRHMkswPhtHkGY", "o79aixAK9nAJT6qDW78CBUV-EqG4", "o79aixEafktJ_REW4uwIQ3RCNSbY",
    "o79aixKN7ZSX_TY386f7WkNorm0I", "o79aixFrhWkYwwwMDwDpfoShmCuQ", "o79aixDLU2e1R-AC8AYyASLFD8DQ",
    "ok8UpwhW5PkK7076PaC-vXF19EEI", "o79aixDHta5eewOHU0XhazHGqkAs", "ok8UpwkJ4OMQB8mIZz8v13yWbZes",
    "o79aixHOvWl19oIhbgxcVSbS5WfI", "o79aixB8M8KUAUS8nAE8-99oFxmU", "o79aixFm8TR4faUhidKPdvOkHH4A",
    "o79aixNE6whFBQirs1JcDkSMI5Kk", "o79aixATBBphnCgCiHrH6iW10Mq4", "o79aixAcQH3zonWE99fKA6ImUoSE",
    "ok8UpwqG051dAyvCpYrr5wuoeZ2Y", "o79aixN9Xexkjx4nZkbUJrtuDmsY", "oKoQnuAo5Tx_LOQkkfpWTjr9ShBc",
    "o79aixN4iPTXz7izOnzvahfugkiU", "o79aixKutpl0bSOfrIf_Kt_4zqqI", "o79aixNaC8YpF17JJlht6NcBlax0",
    "o79aixJWpHR9yiVq1fkcv4FC5YFM", "o79aixJk4bri-7yui_qL_k8Jl7AY", "o79aixBgLjKED4yh-sbSlk3BAihk",
    "o79aixP3Yvl1_-IyHTrIjWG9-9sA", "o79aixECMXycEtBoxPXZbtROO-Ig_00", "ok8UpwqB1ygaeY2yicYAbiTxVBr8",
    "o79aixGh2i6pAeAdIOTU9fIboGZs", "o79aixOVOunbiJaaQo2DFuKRSWvQ", "o79aixE5f1xWSuRXKR5IM9xMZDQM",
    "o79aixPQlJviVwUXw_3sGPBfbbwg", "o79aixKUaEtNdguC4iifidCQOHXs", "o79aixGfvGk4gpr2vAEypKlAyvTk",
    "o79aixAlPMNytw2dJDCuJg1tfw1U", "ok8UpwtDVreYwnsm1qrWX4uKs_KY", "o79aixEsa4B4S8DJPH1OHtq9cn5M",
    "o79aixEXWD107piTau0YoTPhOF1g", "o79aixAsm44wRLxVur3z5pjVmQpg", "o79aixLlTe7kUYfYdaFeQaAiVUqU",
    "o79aixHDsdploYsZ9Edopsf3SelM", "o79aixDS_uR9ADo1WdWd2DCEV1bw", "ok8Upwtzm_X0Os2T8xqCfiAkVOqY",
    "o79aixBGu8V6uCzBDVlbsNOeTsPA", "o79aixMDIvIsJehaoHh9R7YrpDf4", "o79aixAatHpoFDSncGR3J0GoK9iI",
    "o79aixGW9iScD7OlGh6YNbVGxFgo", "o79aixJUsShh67KYpnGUP1G_CWhg", "ok8Upwp5B9js9Ile3bB3upJj3oPY",
    "o79aixMNle7sHyN2FfTz162raBJ4", "o79aixLPueJbMZyPrTaO4e8hmCcI", "o79aixBYG4uOZ1wzIrzNDbEQ37OQ",
    "o79aixF8ITIAcu96kW9erDunhtk4", "o79aixCIX4PT6GeSdoRqzogjMFV8", "o79aixGmW91Yd_ijxStk_3SaLMhQ",
    "o79aixOC0eGQfZkExrkg2MeEwIIw", "o79aixG8eS0gJ2bgUuu-2fH6dw6o", "o79aixNhPwYxA_2zuIx_I9kx1UFI",
    "o79aixLBhocXQxer_WBHqO0Y5RxM", "ok8Upwv7eos_f51Vcr9DA2YsF_Hg", "ok8UpwlyTypNX8hGaOAxrFaFco7c",
    "o79aixM9Y_tALFmPMi36mLzaz9UI", "ok8UpwurF6JiGDserZACKn6B0SB8", "o79aixBErQW6-lERzXagXEd3PbKk",
    "ok8Upwly4zDq8i6YXAt9nhpBlc04", "o79aixF4Kz7olv3x5qJQ4uK7KhxI", "o79aixFJRrctIknKibCRHGsunUx8",
    "oKoQnuCPwuvFL6c_hpfFzYL_Mw-o", "oKoQnuH15qOBBF3pKNEebLcPswKI", "o79aixDf7ZC4Gk1lMiqin2BVgLUk",
    "o79aixPBQVz0ulH9tGfPbCOE4Wl8", "o79aixM88kN1MqtwBNjE1oLVM_v0", "o79aixG07wJmOyknctYsfY2WMBG0",
    "o79aixA4qUeGZ5WpUoXl3kM_6-Gs", "o79aixGqIhuPIUKzVYxlrql9c6T0", "o79aixLcQ-kyGFKpyA8PedqXiWds",
    "o79aixJIrUM3swpqxwjYBFY0bbaM", "o79aixKAcp37qsfcTQ4XwKTmmt-w", "oKoQnuKxiv_TDPDHgPzfv0frQ33k",
    "o79aixDx8MmqAqpC-zuiPScYT3PI", "o79aixKVhSkDZGP3suBR5rZswGms", "ok8UpwqE8cIK6wBoC1-TDnXJoDPE",
    "o79aixD27HNOwB9za4Y6tdl1tQ-g", "o79aixAdRO0F9hsSSuQ9D1f47tbE", "o79aixBsCJTfYi0denQ1a71hUeLQ",
    "o79aixDUap3_YSf6AJmF8umK6swY", "o79aixIrIyyqUKSVW-sj9q4I5aEI", "oKoQnuBol4dvFsAURZhvvB7D4YW8",
    "o79aixNIY45_c_ULrUTiDZ7zls08", "o79aixHSxQc4m0DIHFWvnTP8w3ag", "o79aixK3dxXkivgbKe2e704DApVM",
    "o79aixIzs823HfxsobDaZhV98nbY", "o79aixOmDnuLxmd0CSaqO2ZjZOX0", "o79aixKNlqu-vu_z0ETZe6dy4-Rg",
    "o79aixNeyrcHuzGMv2xwkNjIQ1MM", "o79aixLMbNZn0Myf9GFr_9WfRLW4", "o79aixEk914eO28-4VvvA7yT8kso",
    "o79aixN69GSyLCPz48eIrbgNLMGs", "o79aixB4llYVCJXPYGfB9OyF7L8Q", "oKoQnuG5myymA2-l7x1DSChSEMZI",
    "o79aixIKh7EjdcIg6I82NTbevCkk", "ok8Upwm1G7QZl73S3t7LSAqnK49E", "o79aixK-edF-Qm4J7wzV3QSq22Ds",
    "o79aixFSJh0MJnXFdlbyzK2HQTKM", "o79aixJ782zU1jJDZ8Fqzlm25cTE", "oKoQnuDuGOz89oojhaOn8SAXa7DA",
    "o79aixPDc2u3bmp8lATCA2riPGBc", "o79aixImH68gy4oltZAkw4Iag65s", "o79aixECMXycEtBoxPXZbtROO-Ig",
    "o79aixEIU63tB53X_NDKQ4qK93Sk", "o79aixO2WcYCjdvNyMSWuiS9ILrc", "o79aixDHta5eewOHU0XhazHGqkAst1emp"]


header = {
        'Wxid': "o79aixHf4cFEuY2lnBwDOiNi9qjA",
        'Channel': "wx_anxinjiankang",
        'User-Agent': "micromessenger"
    }


def get_question_form_qa_main(pageSize):
    url = "http://test.anxinyisheng.com/home/question/getIndexStream"
    params = {
        "catalog": 2,
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
    print('查看：' + header["Wxid"] + '-' + qid + '-' + rsp["desc"])


def raise_q(qid):
    url = "http://test.anxinyisheng.com/home/question/raise"
    params = {
        "questionId": qid
    }
    rsp = requests.get(url=url, params=params, headers=header).json()
    print('点赞：' + header["Wxid"] + '-' + qid + '-' + rsp["desc"])


def run():
    m = 0
    qid_list = get_question_form_qa_main(1)
    for i in wxid_list:
        for k in qid_list:
            m += 1
            print(m)
            header["Wxid"] = i
            view_q(k)
            raise_q(k)


run()
