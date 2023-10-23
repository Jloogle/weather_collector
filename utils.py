import logging

import requests

from settings import API_KEY


logging.basicConfig(
    filename='application-log.log',
    filemode='w',
    format='%(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger()


def get_weather(city):
    url = (f"https://api.openweathermap.org/data/2.5/weather?q={city}"
           f"&lang=ru&appid={API_KEY}&units=metric")
    response = requests.get(url)
    return response.json()
