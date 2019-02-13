from django.shortcuts import render, HttpResponse
import random
# from pprint import pprint

# Create your views here.
def index(request):     # request
    # print(request)
    # print(type(request))
    # pprint(request.META)    # http 정보 확인
    return HttpResponse('Welcome to Django!') 
    # view를 만들었지만 url이 없으므로 urls.py로 이동
    
# def dinner(request):
#     menu = ['한식', '중식', '일식', '양식']
#     return HttpResponse(random.choice(menu))
    
def dinner(request):
    menus = ['한식', '중식', '일식', '양식']
    pick = random.choice(menus)
    return render(request, 'dinner.html', {'menus': menus, 'pick': pick})
    
def hello(request, name):
    return render(request, 'hello.html', {'name': name})
    
def cube(request, num):
    nums = num ** 3
    return render(request, 'cube.html', {'num': num, 'nums': nums})
    
def ping(request):
    return render(request, 'ping.html')

def pong(request):
    print(request.GET)
    data = request.GET.get('data')
    return render(request, 'pong.html', {'data': data})
    
def user_new(request):
    return render(request, 'user_new.html')
    
def user_create(request):
    nickname = request.POST.get('nickname')
    pwd = request.POST.get('pwd')
    return render(request, 'user_create.html', {'nickname': nickname, 'pwd': pwd})