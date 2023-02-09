import json
from datetime import datetime
from decouple import config
import requests

API_KEY = config("API_KEY")
LOCATION = config("LOCATION")

url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{LOCATION}?unitGroup=metric&include=current&key={API_KEY}&contentType=json"

location_response = requests.get("http://ipinfo.io/json", timeout=10).text
weather_response = requests.get(url, timeout=10)
weather_raw = weather_response.text
location_data = json.loads(location_response)
weather_data = json.loads(weather_raw)

current_conditions = weather_data["currentConditions"]
temperature = current_conditions["temp"]

date = datetime.now()
timezone = location_data["timezone"]

print(str(date.strftime("%a, %b %-d, %Y, %-I:%M %p")) + " (" + str(timezone) + ")")

print("Current Conditions:")
print(f"Temperature: {temperature:.0f}°C")
