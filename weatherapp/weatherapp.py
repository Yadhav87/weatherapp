import requests
city ="palakkad,IND"
api ="95aee0f01604e46c3a9259c34540b6ad"
#
url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}"
res =requests.get(url).json()
tmp = res['main']['temp']
tmp_c= round(tmp-273.15)
print(f'current temperature in {city}is{tmp_c}°C')
