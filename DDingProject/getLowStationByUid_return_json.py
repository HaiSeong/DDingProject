
import requests
import xml.etree.ElementTree

def getLowStationByUid_return_json(arsId):
    # api 인증키
    key = 'dswkIzbtmtoaVJONYr8kMHJBceWsS8B9SPs8zshw7LlAnQzhDCnNFSI48oQUeHTJBqtn%2FmD6S4i6HDSAUPQ2tQ%3D%3D'

    # getRouteByStation api 호출
    queryParams = 'ServiceKey=' + key + '&arsId=' + arsId
    url = 'http://ws.bus.go.kr/api/rest/stationinfo/getLowStationByUid?' + queryParams

    # xml 파싱을 위한 코드
<<<<<<< HEAD
    req = requests.get(url)
    tree = xml.etree.ElementTree.fromstring(req.text)
    print(req.text)
=======
    req_getLowStationByUid = requests.get(url_getLowStationByUid)
    tree_getLowStationByUid = xml.etree.ElementTree.fromstring(req_getLowStationByUid.text)
    print(req_getLowStationByUid.text)
    '''
    # 정류장의 버스노선ID, 버스노선명 리스트 추출
    busRouteList =[]
    msgBody = tree_getLowStationByUid.find("msgBody")
    itemList = msgBody.findall("itemList")
    for i in itemList: # 버스ID와 버스노선명을 튜플로 저장 : (ID, 노선명)
        busRouteList.append(((i.find("busRouteId").text),i.find("busRouteNm").text))
        
    return busRouteList
    ''''''
    busRouteJson = []
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> parent of 6aa3792 (com)
=======
>>>>>>> parent of 6aa3792b (com)
    msgBody = tree_getLowStationByUid.find("msgBody")
    itemList = msgBody.findall("itemList")


    for i in itemList:
        temp_dict = {}
        temp_dict['busRouteId'] = i.find("busRouteId").text
        temp_dict['busRouteNm'] = i.find("busRouteNm").text
        busRouteJson.append(temp_dict)

    result = dict(zip(map(str,range(len(busRouteJson))), busRouteJson))
    print(result)

    return result
'''

    busRouteList = []
>>>>>>> parent of 6aa3792 (com)
    msgBody = tree_getLowStationByUid.find("msgBody")
    itemList = msgBody.findall("itemList")


    for i in itemList:
        temp_dict = {}
        temp_dict['busRouteId'] = i.find("busRouteId").text
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        temp_dict['busRouteNm'] = i.find("busRouteNm").text
        busRouteJson.append(temp_dict)

    result = dict(zip(map(str,range(len(busRouteJson))), busRouteJson))
    print(result)

    return result
'''

>>>>>>> parent of 6aa3792 (com)
    busRouteList = []
    msgBody = tree.find("msgBody")
    itemList = msgBody.findall("itemList")

    item = msgBody.find("itemList")
    stnNm = item.find("stnNm").text

    for i in itemList:
        temp_dict = {}
        temp_dict['busRouteId'] = i.find("busRouteId").text
=======
>>>>>>> parent of 6aa3792 (com)
=======
>>>>>>> parent of 6aa3792 (com)
=======
>>>>>>> parent of 6aa3792b (com)
        temp_dict['rtNm'] = i.find("rtNm").text

        busRouteList.append(temp_dict)

    result = {'busRouteList':busRouteList,'stnNm':stnNm}
    print(result)

    return result
