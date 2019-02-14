from django.shortcuts import render
from datetime import datetime
import requests
import os

# Create your views here.
def index(request):
    return render(request, 'utilities/index.html')
    
def bye(request):
    today = datetime.now()
    byetime = datetime(2019, 2, 28)
    total = byetime - today
    days = (byetime - today).days
    seconds = (byetime - today).seconds
    return render(request, 'utilities/bye.html', {'total': total, 'days': days, 'seconds': seconds})

def graduation(request):
    today = datetime.now()
    graduationtime = datetime(2019, 5, 28)
    total = graduationtime - today
    days = (graduationtime - today).days
    seconds = (graduationtime - today).seconds
    return render(request, 'utilities/graduation.html', {'total': total, 'days': days, 'seconds': seconds})
    
def imagepick(request):
    return render(request, 'utilities/imagepick.html')
    
def today(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q=Seoul,kr&lang=kr&appid=?'
    data = requests.get(url).json()
    
    description = data["weather"][0]["description"]
    temp = data["main"]["temp"] - 273.15
    return render(request, 'utilities/today.html', {'description': description, 'temp': temp})

def ascii_new(request):
    fonts = ['short', 'utopia', 'rounded', 'acrobatic', 'alligator']
    return render(request, 'utilities/ascii_new.html', {'fonts': fonts})
    
def ascii_make(request):
    text = request.GET.get('text')
    font = request.GET.get('font')
    url = requests.get(f'http://artii.herokuapp.com/make?text={text}&font={font}').text
    return render(request, 'utilities/ascii_make.html', {'text': text, 'font': font, 'url': url})
    
def original(request):
    return render(request, 'utilities/original.html')
    
def translated(request):
    naver_client_id = os.getenv("NAVER_KEY")
    naver_client_secret = os.getenv("NAVER_SECRET")

    papago_url = "https://openapi.naver.com/v1/papago/n2mt"
    # 네이버에 Post 요청을 위해서 필요한 내용들
    headers = {
        "X-Naver-Client-Id": naver_client_id,
        "X-Naver-Client-Secret": naver_client_secret
    }
    data = {
        "source": "ko",
        "target": "en",
        "text": request.POST.get('text')
    }
    papago_response = requests.post(papago_url, headers=headers, data=data).json()
    print(papago_response)
    reply_text = papago_response["message"]["result"]["translatedText"]
    
    # text = request.GET.get('text')
    return render(request, 'utilities/translated.html', {'reply_text': reply_text})