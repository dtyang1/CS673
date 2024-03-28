import requests

def fetch_weather(city_name, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        feels_like = data['main']['feels_like']
        weather_description = data['weather'][0]['description']
        print(f"Weather in {city_name}:")
        print(f"Temperature: {temperature:.2f}\u00B0C")
        print(f"Feels like: {feels_like:.2f}\u00B0C")
        print(f"Description: {weather_description.encode('utf-8').decode('utf-8')}")
    else:
        print("Failed to fetch weather data. Please check the city name or try again later.")

if __name__ == "__main__":
    city_name = input("Enter city name: ")
    api_key = "1748bd65241d54dda7e6aad135a3c14d"
    fetch_weather(city_name, api_key)
