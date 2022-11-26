from assistant.utils.text_to_speech import TextToSpeech
from assistant.utils.weather_details import get_weather_at_city

def main(city_name):
    weather = get_weather_at_city(city_name)
    temperature = weather['temp']['feels_like']
    status = weather['detailed_status']
    response = f"The weather status for '{city_name}' is {status} with an average temprature of '{temperature}' degree farenheit. "
    tts = TextToSpeech(False)
    tts.speak(response)