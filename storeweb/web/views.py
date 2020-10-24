# -*- coding:utf-8 -*-
from django.shortcuts import render
import requests
from django.http.response import HttpResponse
from bs4 import BeautifulSoup
import os
import logging

# Create your views here.
logger =  logging.getLogger(__name__)
base_url = 'http://www.vipxs.la/'
url = 'http://www.vipxs.la/55_55847/'

def index(request):
    return  render(request=request, template_name='index.html')

def get_directory(request):
    result = {}
    for k, v in request.GET.items():
        logger.info(k)
        result[k] = v
    directory = requests.get('http://' + result['url'])
    soup = BeautifulSoup(directory.content,"html.parser",from_encoding="utf-8")
    directory_soup = soup.find('div',id="list")
    return HttpResponse(str(directory_soup).replace('href="/', 'href="%s' % '/get_store_content/?path='))
#     return HttpResponse('<a href="/get_store_content/?name=aaaa">aaaa</a>')

def get_store_content(request):
    result = {}
    for k, v in request.GET.items():
        result[k] = v
    chapter = requests.get(os.path.join(base_url, result['path']))
    chapter_soup = BeautifulSoup(chapter.content, "html.parser", from_encoding="utf-8")
    bookname = str(chapter_soup.find('h1')).replace('<h1>','').replace('</h1>','')
    content = chapter_soup.find('div', id='content')
    bottem1 = chapter_soup.find('div', class_='bottem1')
    bottem = str(bottem1).replace('href="/', 'href="%s' % '/get_store_content/?path=').replace(r'投推荐票', '').replace('章节目录','').replace('加入书签','')
    return HttpResponse('''
    <SCRIPT LANGUAGE=javascript>
    function update(temp)
    {
      if(temp == '#FFFFFF')
      {
        document.body.style.backgroundColor="#FFFFFF";//改变背景色
      }else{
        document.body.style.backgroundColor="#000000";//改变背景色
      }
    }
    </SCRIPT>
    <head>
        <title>%s</title>    
    </head>
    <body style="color:gray;background-color:black;>
        <div style="font-size:40px;color:gray;>
            <h1>%s</h1><br>
        </div>
        <div style="font-size:40px;color:gray;text-align:center;>%s<input type = button value="白天" onclick="update('#FFFFFF')"><input type = button value="夜晚" onclick="update('#000000')"><br></div>
        <div style="font-size:40px;color:gray;>%s<br></div>
        <div style="font-size:40px;color:gray;text-align:center;>%s</div>
        <div><br><br><br></div>
    </body>''' % (bookname, bookname, bottem, content,bottem))

