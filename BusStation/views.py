from django.shortcuts import render
from DDingProject.getLowStationByUid_return_json import *
from DDingProject.getLowStationByUid_return_stId import *
from DDingProject.getLowArrInfoByStIdList import *
from BusStation.forms import *

# Create your views here.
def main(request):
    return render(request, 'main.html')

def getBusList(request):
    if request.method == 'GET':
        arsId = request.GET.get('arsId')
        result = getLowStationByUid_return_json(arsId)
        return render(request, 'busList.html', result)

    elif request.method == 'POST':
        arsId = request.GET.get('arsId')
        busRoute = request.POST['busRoute']
        busRouteId = busRoute.split("'")[3]

        dict_stId = getLowStationByUid_return_stId(arsId)
        stId = dict_stId['stId']
        print(stId)

        temp_dict = dict()
        temp_dict['stId'] = dict_stId['stId']
        temp_dict['busRouteId'] = busRouteId
        data = getLowArrInfoByStIdList(stId,busRouteId)
        vehId1 = data['vehId1']
        if vehId1 == 0:
            return render(request, 'unable.html')
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
    callList = Call.objects.all()

    isCalled = 'false'
    location=""

    if vehId in str(callList.values_list("vehId1")):
        call = Call.objects.filter(vehId1=vehId).order_by('id').first()
        isCalled = 'true'
        location = call.stId
        print(location, "번 정류장에서 요청을 받았습니다.", call, "을 삭제합니다.")
        call.delete()


    call = dict()
    call['isCalled'] = isCalled
    call['location'] = location
    print(call)


    return render(request, 'check.html',{'call':call})
