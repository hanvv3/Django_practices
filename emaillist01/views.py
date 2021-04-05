from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from emaillist01 import models


def index(request):
    results = models.findall()
    data = {'emaillist_list': results}                      # context = 딕셔너리, key를 "results"(value)로 반환
    return render(request, 'emaillist01/index.html', data)      # render(request, template_name, context=None...)
                                                            # context는 dict형으로 원하는 인자(key)를 파이썬 변수로 html페이지로
                                                            # 넘겨줄 수 있음.


def form(request):
    return render(request, 'emaillist01/form.html')


def add(request):
    firstname = request.POST["fn"]                      # eamillist01/form.html에서 POST로 받아온 정보를 다시 파이썬 변수로 넣음
    lastname = request.POST["ln"]
    email = request.POST["email"]

    models.insert(firstname, lastname, email)

    return HttpResponseRedirect("/emaillist01")             # 이메일을 추가하라는 명령을 담은 페이지의 중복 사용을 막기 위해
                                                            # redirct를 사용.


