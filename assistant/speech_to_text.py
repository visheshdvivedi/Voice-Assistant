import speech_recognition as sr
from assistant.console_manager import ConsoleManager

class SpeechToText:
    
    @staticmethod
    def listen():
        try:
            recognizer = sr.Recognizer()
            with sr.Microphone() as source:
                print("User: ", end="")
                audio = recognizer.listen(source)
                text = recognizer.recognize_google(audio)
                print(text)
                return text
        expect sr.UnknownValueError:
            ConsoleManager.print_error("Could not understand voice")
            exit(0)
        except sr.RequestError:
            ConsoleManager.print_error("No internet connection available")
            exit(0)