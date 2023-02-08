from decouple import config
import requests
import json

api_key = config("API_KEY")

url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Mae%20Chan?unitGroup=metric&include=current&key={api_key}&contentType=json"

response = requests.get(url)
text = response.text

weather_data = json.loads(text)
print(weather_data["currentConditions"])

current_conditions = weather_data["currentConditions"]
temperature = current_conditions["temp"]

print(f" |  {temperature:.0f}°C  |")
