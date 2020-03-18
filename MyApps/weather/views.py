from django.shortcuts import render
from django.http import HttpResponseRedirect
import requests
from .models import savedLocations
# Create your views here.
def index(request):
    #for every saved location find weather info
    locs = savedLocations.objects.all()
    locations = []
    for loc in locs:
        locations.append(getWeather(loc))
    return render(request, 'weather/index.html', {'locations' : locations })

def getWeather(city):
    #build the url
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=c21807537671ed836a423612bca624e8'.format(city)
    #query result
    query = requests.get(url).json()
    #get the city_name, city_temp, temp description and then icon name pair for weather description
    city_name = query['name']
    city_temp = int(query['main']['temp'] - 273.15)
    city_temp_desc = query['weather'][0]['description']
    city_temp_icon = query['weather'][0]['icon']
    return {'id': city.id, 'city': city_name, 'temp': city_temp, 'desc': city_temp_desc, 'icon': city_temp_icon}

def addCity(request):
    #add a city
    city = request.POST.get('city')
    #create the object and try to get weather info
    new_item = savedLocations(location=city)
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=c21807537671ed836a423612bca624e8'.format(city)
    query = requests.get(url).json()
    #if query returns message then an error occured
    if('message' in query.keys() and query['message'] == 'city not found'):
        error_message = 'city not found'
        return HttpResponseRedirect('../', {'error_message': error_message })
    #else everything is ok. Location is saved and return to index
    else:
        new_item.save()
        return HttpResponseRedirect('../')

#get the city id and delete from saved locations
def deleteCity(request, city_id):
    delCity = savedLocations.objects.get(pk=city_id)
    delCity.delete()
    return HttpResponseRedirect('../')