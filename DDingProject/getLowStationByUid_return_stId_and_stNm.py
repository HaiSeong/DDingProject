
import requests
import xml.etree.ElementTree

def getLowStationByUid_return_stId_and_stNm(arsId):
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

    result_dict = dict()
    for i in itemList:
        if i.find("arsId").text == arsId:
            result_dict['stId'] = i.find("stId").text
            result_dict['stnNm'] = i.find("stnNm").text

    print(result_dict)
    return result_dict
