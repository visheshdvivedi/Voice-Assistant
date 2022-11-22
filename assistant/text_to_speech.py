import pyttsx3
from assistant.console_manager import ConsoleManager

class TextToSpeech:
    def __init__(self):
        self._engine = pyttsx3.init()
        self._engine.setProperty("rate", 130)
        self._engine.setProperty("volume", 0.5)

    def speak(self, message):
        try:    
            self._engine.say(message)
            self._engine.runAndWait()
        except:
            ConsoleManager.print_error("Bot is unable to speak")
            exit(0)