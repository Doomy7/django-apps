from django.shortcuts import render
from django.http import HttpResponseRedirect
import requests
from .models import savedLocations
# Create your views here.
def index(request):
    locs = savedLocations.objects.all()
    locations = []
    for loc in locs:
        locations.append(getWeather(loc))
    return render(request, 'weather/index.html', {'locations' : locations })

def getWeather(city):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={placeholderforapikey}'.format(city)
    query = requests.get(url).json()
    city_name = query['name']
    city_temp = int(query['main']['temp'] - 273.15)
    city_temp_desc = query['weather'][0]['description']
    city_temp_icon = query['weather'][0]['icon']
    return {'id': city.id, 'city': city_name, 'temp': city_temp, 'desc': city_temp_desc, 'icon': city_temp_icon}

def addCity(request):
    city = request.POST.get('city')
    new_item = savedLocations(location=city)
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={placeholderforapikey}'.format(city)
    query = requests.get(url).json()
    if('message' in query.keys() and query['message'] == 'city not found'):
        error_message = 'city not found'
        return HttpResponseRedirect('../', {'error_message': error_message })
    else:
        new_item.save()
        return HttpResponseRedirect('../')

def deleteCity(request, city_id):
    delCity = savedLocations.objects.get(pk=city_id)
    delCity.delete()
    return HttpResponseRedirect('../')