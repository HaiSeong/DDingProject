
import requests
import xml.etree.ElementTree

def getLowStationByUid_return_stId_and_stNm(arsId):
    # api 인증키
    key = 'dswkIzbtmtoaVJONYr8kMHJBceWsS8B9SPs8zshw7LlAnQzhDCnNFSI48oQUeHTJBqtn%2FmD6S4i6HDSAUPQ2tQ%3D%3D'

    # getRouteByStation api 호출
    queryParams = 'ServiceKey=' + key + '&arsId=' + arsId
    url = 'http://ws.bus.go.kr/api/rest/stationinfo/getLowStationByUid?' + queryParams

    # xml 파싱을 위한 코드
    req = requests.get(url)
    tree = xml.etree.ElementTree.fromstring(req.text)
    print(req.text)
    msgBody = tree.find("msgBody")
    itemList = msgBody.findall("itemList")

    result_dict = dict()
    for i in itemList:
        if i.find("arsId").text == arsId:
            # 버스 정류장 아이디
            result_dict['stId'] = i.find("stId").text
            # 버스 정류장 이름
            result_dict['stnNm'] = i.find("stnNm").text

    print(result_dict)
    return result_dict
