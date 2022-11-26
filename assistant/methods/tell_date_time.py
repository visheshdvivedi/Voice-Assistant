from datetime import datetime
from assistant.utils.text_to_speech import TextToSpeech

WEEKDAYS = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

MONTH_NAME = [
    "",
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    now = datetime.now()
    hour = now.hour
    minute = now.minute
    day = WEEKDAYS[now.weekday()]
    date = now.day
    month = MONTH_NAME[now.month]
    year = now.year

    response = f"It's {hour}:{minute} on {day}, {date} {month} {year}"

    tts = TextToSpeech(False)
    tts.speak(response)