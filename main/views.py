import urllib.request 
import json
from django.shortcuts import render 

# Create your views here.

def index(request):
    if request.method == 'POST':
        city = request.POST["city"]

        try:
            source = urllib.request.urlopen(
                f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=your_appid_key_here"
            ).read()
            data = json.loads(source)

            name = data["name"]
            temperature = data["main"]["temp"]
            condition = data["weather"][0]["main"]
            description = data["weather"][0]["description"]
            humidity = data["main"]["humidity"]

            clData = {
                "name": name,
                "temperature": temperature - 273.15,
                "condition": condition,
                "description": description,
                "humidity": humidity,
            }
        except urllib.error.URLError:
            clData = {
                "error": "City not found"
            }
        except KeyError:
            clData = {
                "error": "Invalid city name"
            }
        except Exception as e:
            clData = {
                "error": str(e)
            }

    else:
        clData = {}

    return render(request, "main/index.html", clData)