from datetime import date
from django.shortcuts import render
import requests


def home(request):

    city = request.GET.get('city', 'Lucknow')
    urls = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=a53fece9b59cc8b6113413929f386c57'
    data = requests.get(urls).json()
    

    payload = {
        'city' : data['name'],
        'weather' : data['weather'][0]['main'] , 
        'icon' : data['weather'][0]['icon'] ,
        'kelvin_temperature' : data['main']['temp'] ,
        'celsius_temperature' : int(data['main']['temp'] -273) ,
        'pressure' : data['main']['pressure'] ,
        'humidity': data['main']['humidity'] ,
        'description' : data['weather'][0]['description'] ,

    }
    context = {'data':payload}
    print(context)
    return render(request,'home.html',context)
