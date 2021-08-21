
import requests
import xml.etree.ElementTree

def getLowStationByUid_return_json(arsId):
    # api 인증키
    key = 'dswkIzbtmtoaVJONYr8kMHJBceWsS8B9SPs8zshw7LlAnQzhDCnNFSI48oQUeHTJBqtn%2FmD6S4i6HDSAUPQ2tQ%3D%3D'

    # getRouteByStation api 호출
    queryParams = 'ServiceKey=' + key + '&arsId=' + arsId
    url = 'http://ws.bus.go.kr/api/rest/stationinfo/getLowStationByUid?' + queryParams

    # xml 파싱을 위한 코드
    req = requests.get(url)
    tree = xml.etree.ElementTree.fromstring(req.text)
    print(req.text)
    busRouteList = []
    msgBody = tree.find("msgBody")
    itemList = msgBody.findall("itemList")

    # 버스 정류소 이름
    stnNm = itemList[0].find("stnNm").text

    for i in itemList:
        temp_dict = {}
        # 버스 노선 아이디
        temp_dict['busRouteId'] = i.find("busRouteId").text
        # 버스 루트 이름
        temp_dict['rtNm'] = i.find("rtNm").text
        busRouteList.append(temp_dict)

    result = {'busRouteList':busRouteList, 'stnNm':stnNm}
    print(result)

    return result
