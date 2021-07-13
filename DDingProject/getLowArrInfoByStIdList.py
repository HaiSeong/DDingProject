
import requests
import xml.etree.ElementTree

def getLowArrInfoByStIdList(stId, busRouteId):
    # api 인증키
    key = 'dswkIzbtmtoaVJONYr8kMHJBceWsS8B9SPs8zshw7LlAnQzhDCnNFSI48oQUeHTJBqtn%2FmD6S4i6HDSAUPQ2tQ%3D%3D'

    # getRouteByStation api 호출
    queryParams_getLowArrInfoByStIdList = 'ServiceKey=' + key + '&stId=' + stId
    url_getLowArrInfoByStIdList = 'http://ws.bus.go.kr/api/rest/arrive/getLowArrInfoByStId?' + queryParams_getLowArrInfoByStIdList

    # xml 파싱을 위한 코드
    req_getLowArrInfoByStIdList = requests.get(url_getLowArrInfoByStIdList)
    tree_getLowArrInfoByStIdList = xml.etree.ElementTree.fromstring(req_getLowArrInfoByStIdList.text)\


    msgBody = tree_getLowArrInfoByStIdList.find("msgBody")
    itemList = msgBody.findall("itemList")

    result_dict = dict()
    for i in itemList:
        if busRouteId == i.find("busRouteId").text:
            result_dict['plainNo1'] = i.find("plainNo1").text
            result_dict['vehId1'] = i.find("vehId1").text
            result_dict['exps1'] = i.find("exps1").text
            result_dict['rtNm'] = i.find("rtNm").text

    print(result_dict)
    return result_dict
