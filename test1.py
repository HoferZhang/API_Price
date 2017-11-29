import requests
import json


url_DocIndex = "http://test.anxinyisheng.com/home/user/doc_detail"

headers = {
    "Wxid":"o79aixECshqXft8Cck5fMC7LdYZs",
    "Channel": "wx_anxinjiankang",
    "User-Agent": "micromessenger"}
paramDocIndex = {
    "_id": "59c4fe257f1008c12c8b4579",
    "bizid": "573ae98d7f10087a048b4a61",
    "from": "doctor_list"}

rspDocIndex = requests.get(url=url_DocIndex, params=paramDocIndex, headers=headers)

rspJson = json.loads(rspDocIndex.text)
docID = rspJson["msg"]["_id"]
docName = rspJson["msg"]["name"]
consultPrice = rspJson["msg"]["priceList"]["consultationPrice"]
qaPrice = rspJson["msg"]["priceList"]["qaPrice"]

print (rspDocIndex.status_code)
print (rspDocIndex.text)
print (rspDocIndex.text)
