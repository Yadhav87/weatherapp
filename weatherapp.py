import requests

api_key = '95aee0f01604e46c3a9259c34540b6ad'

user_input = input("Enter city: ")

weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city.name}&appid={API.key}")

if weather_data.json()['cod'] == '404':
    print("No City Found")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])

    print(f"The weather in {user_input} is: {weather}")
    print(f"The temperature in {user_input} is: {temp}ºF")