'''
Created on 2020��10��6��

@author: wqx
'''
from django.urls.conf import path
from django.contrib import admin
from web import views
from django.conf.urls import url

app_name = 'web'  # ������Ϊ��url���������

urlpatterns=[
    path('admin/', admin.site.urls),
    path('index/', views.index),
    url(r'^get_directory/', views.get_directory),
    url(r'^get_store_content/', views.get_store_content),
    ]