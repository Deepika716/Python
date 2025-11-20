import requests

city = input("Enter city name: ")
url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"

loc = requests.get(url).json()
if "results" not in loc:
    print("City not found")
    exit()

lat = loc["results"][0]["latitude"]
lon = loc["results"][0]["longitude"]

weather = requests.get(
    f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
).json()

print(f"Current temp in {city}: {weather['current_weather']['temperature']}°C")
