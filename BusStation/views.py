from django.shortcuts import render
from DDingProject.getLowStationByUid_return_json import *
from DDingProject.getLowStationByUid_return_stId_and_stNm import *
from DDingProject.getLowArrInfoByStIdList import *
from BusStation.forms import *

# Create your views here.
def main(request):
    return render(request, 'main.html')

def getBusList(request):
    # 버스 호출 선택 사이트에 접속했을때
    if request.method == 'GET':
        # arsId(버스 정류장 아이디)를 인자로 전달
        arsId = request.GET.get('arsId')
        # getLowStationByUid_return_json함수 사용
        # (arsId를 인자로 받아서 busRouteId(버스 노선 아이디)와 rtNm(버스 노선 이름)을 딕셔너리 타입으로 반환해주는 함수)
        result = getLowStationByUid_return_json(arsId)
        # 받은 결과값을 버스 호출 페이지에 전달해서 화면 출력
        return render(request, 'busList.html', result)

    # 버스를 선택했을때
    elif request.method == 'POST':
        arsId = request.GET.get('arsId')
        busRoute = request.POST['busRoute']
        busRouteId = busRoute.split("'")[3]

        # getLowStationByUid_return_stId_and_stNm 사용
        # (arsId를 인자로 받아서 stId(버스 정류장 아이디)와 stnNm(버스 정류장 이름)을 딕셔너리 타입으로 반환해주는 함수)
        dict_stId = getLowStationByUid_return_stId_and_stNm(arsId)
        stId = dict_stId['stId']
        stnNm = dict_stId['stnNm']
        print(stId)
        print(stnNm)

        # 호출 정보를 저장하기위한 빈 딕셔너리 생성
        temp_dict = dict()
        temp_dict['stId'] = stId
        temp_dict['stnNm'] = stnNm
        temp_dict['busRouteId'] = busRouteId
        # getLowArrInfoByStIdList 사용
        # (stId와 busRouteId를 인자로 받아서 plainNo1(버스 번호판 번호), vehId1(버스 식별 번호), exps1(남은 시간), rtNm(노선 이름)을 딕셔너리 타입으로 반환해주는 함수)
        data = getLowArrInfoByStIdList(stId,busRouteId)
        vehId1 = data['vehId1']
        print(vehId1)
        temp_dict['vehId1'] = vehId1

        # getLowArrInfoByStIdList으로 생성된 딕셔너리를 폼에 저장
        form=Form(temp_dict)

        # 폼이 유요한지 판단 후 유효하면 DB에 저장
        if form.is_valid():
            form.save()
            print(Call.objects.all().values())
            print(busRouteId)
            # 선택완료 페이지에 data전달 후 페이지 출력
            return render(request, 'selected.html', {'data':data})


# 호출 DB를 보여주는 함수
def list(request):
    callList = Call.objects.all()
    return render(request, 'list.html',{'callList':callList})


# 버스가 자신이 호출되었는지 확인하는 함수
def check(request):
    # 버스 자신의 식별 번호(vehId)를 인자로 전달
    vehId = request.GET.get('vehId')
    print(vehId)

    isCalled = 'false'
    location = " " # == stId
    stnNm = " "

    # 호출 DB에 자신의 식별번호(vehId)가 존재한다면
    if vehId in str(Call.objects.values_list("vehId1")):
        # 호출된 정보를 저장
        call = Call.objects.filter(vehId1=vehId).order_by('id').first()
        isCalled = 'true'
        location = call.stId # == stId
        stnNm = call.stnNm
        print(location, "번 정류장에서 요청을 받았습니다.", call, "을 삭제합니다.")
        # DB에서 요청을 삭제
        call.delete()

    # 저장된 정보를 딕셔너리로 저장
    call = dict()
    call['isCalled'] = isCalled
    call['location'] = location
    call['stnNm'] = stnNm
    print(call)

    # check 페이지로 정보 전달
    return render(request, 'check.html',{'call':call})
