from django.shortcuts import render

import urllib.request
import json


def index(request):

    if request.method == 'POST':
        city = request.POST['city']

        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=8547811b1a65df0b450516ebe518c8a2').read()

        #convert json file from api to dictionary
        list_data = json.loads(source)    #it loads all source argument 

        #create data dict it will be render on htpp page
        data = {
            "country_code" : str(list_data['sys']['country']),
            "coordinate" : str(list_data['coord']['lon']) + ', ' 
            + str(list_data['coord']['lat']),

            "temp" : str(list_data['main']['temp']) + ' °C',
            "temp_min" : str(list_data['main']['temp_min'])+ ' °C',
            "temp_max" : str(list_data['main']['temp_max'] )+ ' °C',
            "pressure" : str(list_data['main']['pressure']),
            "humidity" : str(list_data['main']['humidity']),
            "main" : str(list_data['weather'][0]['main']),
            "icon" : list_data['weather'][0]['icon'],

        }
        print(data) # it shows in terminal
    else:
        data = {} # just empty
    
    return render(request, "main/index.html", data) #return on website http
    
    