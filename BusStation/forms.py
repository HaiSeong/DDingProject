from django.forms import ModelForm
from BusStation.models import *

# 호출 폼 정의
class Form(ModelForm):
    class Meta:
        model = Call
        fields=['stId','stnNm','busRouteId','vehId1']