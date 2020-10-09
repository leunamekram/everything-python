# import requests
from pynotifier import Notification

# url = "http://api.openweathermap.org/data/2.5/weather?q="
# cityname = "biclatan"
# api_key = ""

# data = requests.get(url+cityname+'&appid'=+api_key).json()

# city = data['name']
# country = data['sys']['country']
# temperature = data['main']['temp_max'] - 273.15
# weather = data['weather'][0]['main']
# wind_speed = float(data['wind']['speed'])
# humidity = data['main']['humidity']
# pressure = data['main']['pressure']

# if data['cod'] != '404':
if True:
    Notification(
        title = 'Biclatan, General Trias, Philippines',
        description = f'Test Notification',
        duration = 10,
        icon_path = 'Picture1.ico',
        urgency = Notification.URGENCY_CRITICAL).send()
