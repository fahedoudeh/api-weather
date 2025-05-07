import requests



def get_weather_data(city_name, api_key):
    # API-endpoint
    url = (f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric")

    #Http GET request om data op te halen
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code} - {response.text}")

def display_weather_info(weather_data):
    city = weather_data["name"]
    temp = weather_data["main"]["temp"]
    description = weather_data["weather"][0]["description"]
    humidity = weather_data["main"]["humidity"]
    wind_speed = weather_data["wind"]["speed"]

    print(f"Weather in {city}:")
    print(f"Temperature: {temp}°C")
    print(f"Description: {description.capitalize()}")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")




api_key = "d6e205d1e4a404e57500568b85768c29"

city_name = input("Enter city name: ").strip()

while not city_name:
    print("City name cannot be empty")
    city_name= input("Enter city name").strip()

weather_data = get_weather_data(city_name, api_key)
display_weather_info(weather_data)