from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def hello1(request):
#   print('ok!!!!!')
    html = '<h1>Hello World1</h1><h2>안녕 세상</h2>'
    return HttpResponse(html, content_type='text/html; charset=utf-8')


def hello2(request):
#   results = model.findall()
    return render(request, 'helloworld/hello2.html')


def tags(request):
    return render(request, 'helloworld/tags.html')


