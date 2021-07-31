"""DDingProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from BusStation.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', main),

    # 버스 호출을 위한 페이지
    path('getBusList/', getBusList),

    # 호출 요청을 보기위한 페이지
    path('list/', list),

    # 버스가 호출을 받는 페이지
    path('check/', check),
]
