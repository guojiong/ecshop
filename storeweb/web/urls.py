'''
Created on 2020年10月6日

@author: wqx
'''
from django.urls.conf import path
from django.contrib import admin
from web import views
from django.conf.urls import url

app_name = 'web'  # 这里是为了url反向解析用

urlpatterns=[
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path(r'get_directory/', views.get_directory),
    url(r'^get_store_content/', views.get_store_content),
    ]