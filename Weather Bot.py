import requests
import time

city_Name = input("Please enter the name of the City you woud like to know the weather of")

r = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city_Name+"&appid=37d99f4c8bd8fa96d4509c54c8a262d7")

data = r.json()
print(r.status_code)

time.sleep(3)

if r.status_code == 200:
    print((data['main']['temp'] - 273.15)//1,'Degrees Celcius')
else:
    print('Please enter a valid city name')

