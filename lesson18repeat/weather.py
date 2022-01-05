import requests
from pprint import pprint

params = {
    'appid': 'd0c4c1e4babd454e692db213ba832310',
    'units': 'metric',
    'lang': 'ru'
}
params['q'] = 'tashkent'

weather = requests.get('http://api.openweathermap.org/data/2.5/weather?', params=params).json()
pprint(weather)
