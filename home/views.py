from django.shortcuts import render, HttpResponse
# from pprint import pprint

# Create your views here.
def index(request):     # request
    # print(request)
    # print(type(request))
    # pprint(request.META)    # http 정보 확인
    return HttpResponse('Welcome to Django!') 
    # view를 만들었지만 url이 없으므로 urls.py로 이동