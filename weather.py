import requests



def get_weather_data(city_name, api_key):
    url = (f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric')
    response = requests.get(url)
    return response

def print_weather_data(data_dict):
    print(f"City: {data_dict['name']}")
    print(f"Country: {data_dict['sys']['country']}")
    print(f"Weather: {data_dict['weather'][0]['main']}")
    print(f"Description: {data_dict['weather'][0]['description']}")
    print(f"Temp: {data_dict['main']['temp']} Degrees")

city_name = input("Enter a city name: ")
api_key = 'd6e205d1e4a404e57500568b85768c29'

weather_data = get_weather_data(city_name, api_key)

weather_data_dict = weather_data.json()

if weather_data.status_code == 200:
    print("Success!")
else:
    print(f"Something went wrong: {weather_data.status_code}")

print_weather_data(weather_data_dict)