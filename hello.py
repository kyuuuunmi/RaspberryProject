import json, requests

url = 'http://m.bus.go.kr/mBus/bus/getStationByUid.bms'
urlwheather = 'http://www.kma.go.kr/wid/queryDFS.jsp'
params = dict(
   arsId='09107'
)
paramswheather = dict(
    gridx = '61',
    gridy = '125'
)

resp = requests.get(url=url, params=params)
data = json.loads(resp.text)

# respw = requests.get(url=urlwheather, params=paramswheather)
# dataw = json.loads(respw.text)
#
# print(dataw)
print(data)
print(data['resultList'][1]['rtNm'])

print(data['resultList'][1]['sectNm'])
print(data['resultList'][7]['arrmsg1'])

for i in data['resultList']:
    print(i['sectNm'])
    print(i['arrmsg1'])
    print(i['rtNm'])



#for route in data['resultList']:



# print(data)
# print(data["rtNm"])c
#
# let
# data = JSON(value)
# // print(data)
#
# if let name = data["name"].string{
# self.txtName.text = name
# }