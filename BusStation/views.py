from django.shortcuts import render
from DDingProject.getLowStationByUid_return_json import *
from DDingProject.getLowStationByUid_return_stId_and_stNm import *
from DDingProject.getLowArrInfoByStIdList import *
from BusStation.forms import *

# Create your views here.
def main(request):
    return render(request, 'main.html')

def getBusList(request):
    if request.method == 'GET':
        arsId = request.GET.get('arsId')
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        # getLowStationByUid_return_json함수 사용
        # (arsId를 인자로 받아서 busRouteId(버스 노선 아이디)와
        # rtNm(버스 노선 이름)을 딕셔너리 타입으로 반환해주는 함수)
=======
>>>>>>> parent of 6aa3792 (com)
=======
>>>>>>> parent of 6aa3792 (com)
=======
>>>>>>> parent of 6aa3792 (com)
        result = getLowStationByUid_return_json(arsId)
        return render(request, 'busList.html', result)

    elif request.method == 'POST':
        arsId = request.GET.get('arsId')
        busRoute = request.POST['busRoute']
        busRouteId = busRoute.split("'")[3]

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        # getLowStationByUid_return_stId_and_stNm 사용
        # (arsId를 인자로 받아서 stId(버스 정류장 아이디)와
        # stnNm(버스 정류장 이름)을 딕셔너리 타입으로 반환해주는 함수)
=======
>>>>>>> parent of 6aa3792 (com)
=======
>>>>>>> parent of 6aa3792 (com)
=======
>>>>>>> parent of 6aa3792 (com)
        dict_stId = getLowStationByUid_return_stId_and_stNm(arsId)
        stId = dict_stId['stId']
        stnNm = dict_stId['stnNm']
        print(stId)
        print(stnNm)

        temp_dict = dict()
        temp_dict['stId'] = stId
        temp_dict['stnNm'] = stnNm
        temp_dict['busRouteId'] = busRouteId
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        # getLowArrInfoByStIdList 사용
        # (stId와 busRouteId를 인자로 받아서
        # plainNo1(버스 번호판 번호), vehId1(버스 식별 번호)
        # , exps1(남은 시간), rtNm(노선 이름)을 딕셔너리 타입으로 반환해주는 함수)
=======
>>>>>>> parent of 6aa3792 (com)
=======
>>>>>>> parent of 6aa3792 (com)
=======
>>>>>>> parent of 6aa3792 (com)
        data = getLowArrInfoByStIdList(stId,busRouteId)
        vehId1 = data['vehId1']
        print(vehId1)
        temp_dict['vehId1'] = vehId1
        form=Form(temp_dict)

        if form.is_valid():
            form.save()
            print(Call.objects.all().values())
            print(busRouteId)
            return render(request, 'selected.html', {'data':data})


def list(request):
    callList = Call.objects.all()
    return render(request, 'list.html',{'callList':callList})


def check(request):
    vehId = request.GET.get('vehId')
    print(vehId)

    isCalled = 'false'
    location = " " # == stId
    stnNm = " "

    if vehId in str(Call.objects.values_list("vehId1")):
        call = Call.objects.filter(vehId1=vehId).order_by('id').first()
        isCalled = 'true'
        location = call.stId
        stnNm = call.stnNm
        print(location, "번 정류장에서 요청을 받았습니다.", call, "을 삭제합니다.")
        call.delete()


    call = dict()
    call['isCalled'] = isCalled
    call['location'] = location
    call['stnNm'] = stnNm
    print(call)


    return render(request, 'check.html',{'call':call})
