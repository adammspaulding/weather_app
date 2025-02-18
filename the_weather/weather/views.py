from django.shortcuts import render, redirect
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
        if form.is_valid():
            form.save()
    
    form = CityForm()
    
    weather_data = []
    
    api_key = os.getenv('API_KEY')
    
    for city in cities:
        city_weather = requests.get(url.format(city, api_key)).json()
        
        if 'main' in city_weather:
            weather = {
                'city': city,
                'temperature': city_weather['main']['temp'],
                'description': city_weather['weather'][0]['description'],
                'icon': city_weather['weather'][0]['icon']
            }
            weather_data.append(weather)
        else:
            # Handle the case where the city is not found or API response is invalid
            weather = {
                'city': city,
                'temperature': 'N/A',
                'description': 'City not found',
                'icon': 'N/A'
            }
            weather_data.append(weather)
    
    context = {'weather_data': weather_data, 'form': form}
    
    return render(request, 'weather/index.html', context)

def delete_city(request, city_id):
    City.objects.get(id=city_id).delete()
    return redirect('index')