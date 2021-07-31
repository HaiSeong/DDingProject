
import requests
import xml.etree.ElementTree

def getLowStationByUid_return_json(arsId):
    # api 인증키
    key = 'dswkIzbtmtoaVJONYr8kMHJBceWsS8B9SPs8zshw7LlAnQzhDCnNFSI48oQUeHTJBqtn%2FmD6S4i6HDSAUPQ2tQ%3D%3D'

    # getRouteByStation api 호출
    queryParams_getLowStationByUid = 'ServiceKey=' + key + '&arsId=' + arsId
    url_getLowStationByUid = 'http://ws.bus.go.kr/api/rest/stationinfo/getLowStationByUid?' + queryParams_getLowStationByUid

    # xml 파싱을 위한 코드
    req_getLowStationByUid = requests.get(url_getLowStationByUid)
    tree_getLowStationByUid = xml.etree.ElementTree.fromstring(req_getLowStationByUid.text)
    print(req_getLowStationByUid.text)
    busRouteList = []
    msgBody = tree_getLowStationByUid.find("msgBody")
    itemList = msgBody.findall("itemList")


    for i in itemList:
        temp_dict = {}
        # 버스 노선 아이디
        temp_dict['busRouteId'] = i.find("busRouteId").text
        # 버스 루트 이름
        temp_dict['rtNm'] = i.find("rtNm").text
        busRouteList.append(temp_dict)

    result = {'busRouteList':busRouteList}
    print(result)

    return result
