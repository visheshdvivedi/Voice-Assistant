import random
import wikipedia
from assistant.utils.text_to_speech import TextToSpeech

def search_wikipedia(search_term):
    tts = TextToSpeech(False)
    results, raw_results = wikipedia.search(search_term, results=1, suggestion=True)
    
    if len(results) == 0:
        tts.speak(f"I couldn't find any wikipedia article for '{search_term}'")
        return

    term = results[0]
    try:
        page = wikipedia.page(term)
        return page.summary
        summary = page.summary.split(".")
        for line in summary[:3]:
            tts.speak(line)
    except wikipedia.exceptions.DisambiguationError as error:
        page = wikipedia.page(error.options[0])
        return page.summary
        summary = page.summary.split(".")
        for line in summary[:3]:
            tts.speak(line)