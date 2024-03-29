"""django_intro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from pages import views # 생성한 앱 pages 폴더 안의 views.py 파일

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index), # url 경로 마지막에 /를 붙이는 습관! 
    path('introduce/<str:name>/<int:age>/', views.introduce),
    path('dinner/',views.dinner),
    path('image/', views.image),
    path('hello/<str:name>/', views.hello), # name이라는 값을 받고 str 형태임을 의미
    path('times/<int:num1>/<int:num2>/', views.times),
    path('circle/<int:num>/', views.circle),
    path('template_language/', views.template_language),
    path('isbirth/', views.isbirth),
    path('ispal/<str:word>/',views.ispal),
]
