from django.forms import ModelForm
from BusStation.models import *

class Form(ModelForm):
    class Meta:
        model = Call
        fields=['stId','stnNm','busRouteId','vehId1']