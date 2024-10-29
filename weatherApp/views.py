from django.shortcuts import render
import json
import urllib.request

# Create your views here.
def indexView(request):
    if request.method == "POST":
        city = request.POST['city']
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&APPID=5c06753ea6edff1007c1c28521e97764').read()
        json_data = json.loads(res)
        cityData = {
            "name": json_data['name'],
            "temperature": json_data['main']['temp'],
            "pressure": json_data['main']['pressure'],
            "humidity": json_data['main']['humidity'],
            
        }
    else:
        cityData = {}
    return render(request, 'index.html', cityData)