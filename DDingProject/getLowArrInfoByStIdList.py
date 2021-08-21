
import requests
import xml.etree.ElementTree

def getLowArrInfoByStIdList(stId, busRouteId):
    # api 인증키
    key = 'dswkIzbtmtoaVJONYr8kMHJBceWsS8B9SPs8zshw7LlAnQzhDCnNFSI48oQUeHTJBqtn%2FmD6S4i6HDSAUPQ2tQ%3D%3D'

    # getRouteByStation api 호출
    queryParams = 'ServiceKey=' + key + '&stId=' + stId
    url = 'http://ws.bus.go.kr/api/rest/arrive/getLowArrInfoByStId?' + queryParams

    # xml 파싱을 위한 코드
    req = requests.get(url)
    tree = xml.etree.ElementTree.fromstring(req.text)
    msgBody = tree.find("msgBody")
    itemList = msgBody.findall("itemList")

    # 결과 출력을 위한 빈 딕셔너리 타입 생성
    result_dict = dict()
    for i in itemList:
        if busRouteId == i.find("busRouteId").text:
            # 버스 번호판 번호
            result_dict['plainNo1'] = i.find("plainNo1").text
            # 버스 식별 번호
            result_dict['vehId1'] = i.find("vehId1").text
            # 남은 시간
            result_dict['exps1'] = i.find("exps1").text
            # 노선 이름
            result_dict['rtNm'] = i.find("rtNm").text

    print(result_dict)
    return result_dict

