from assistant.utils.text_to_speech import TextToSpeech
from assistant.utils.wikipedia_search import search_wikipedia

def main(search_term):
    tts = TextToSpeech(False)
    results = search_wikipedia(search_term)
    for line in results.split(".")[:3]:
        tts.speak(line)