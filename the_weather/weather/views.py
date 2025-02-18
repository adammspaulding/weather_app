from django.shortcuts import render
import requests
import os
from dotenv import load_dotenv
from .models import City
from .forms import CityForm

load_dotenv()

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={}'
    
    cities = City.objects.all()
    
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()
    
    form = CityForm()
    
    weather_data = []
    
    api_key = os.getenv('API_KEY')
    
    for city in cities:
            
        city_weather = requests.get(url.format(city, api_key)).json()
        
        weather = {
            'city': city,
            'temperature':city_weather['main']['temp'],
            'description':city_weather['weather'][0]['description'],
            'icon':city_weather['weather'][0]['icon']
        }
        
        weather_data.append(weather)
    
    context = {'weather_data':weather_data, 'form':form}
    
    return render(request, 'weather/index.html', context)
