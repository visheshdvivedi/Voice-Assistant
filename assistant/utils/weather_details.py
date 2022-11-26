import random
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

PYOWM_API_KEY = "607066b9505d3aac060dcd85b7adf87e"

def get_weather_at_city(city_name):
    owm = OWM(PYOWM_API_KEY)
    manager = owm.weather_manager()
    obs = manager.weather_at_place(city_name)
    weather = obs.weather
    return weather.__dict__