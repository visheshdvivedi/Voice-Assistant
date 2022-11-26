import speech_recognition as sr
from assistant.console_manager import ConsoleManager as console

stop_listener = None
is_awake = False

def listen_awake_callback(recognizer, audio):
    try:
        global is_awake

        text = recognizer.recognize_google(audio)
        console.print_user_chat(text)
        if "jarvis" in text.lower():
            if stop_listener != None:
                stop_listener(False)
                is_awake = True
                return
    except sr.UnknownValueError:
        pass
    except SystemExit:
        print("Exiting ...")
        exit(0)

class SpeechToText:
    def __init__(self, initialize_message=False):

        if initialize_message:
            console.print_info("Initializing speech to text drive...", True)

        try:
            self._recognizer = sr.Recognizer()
            self._microphone = sr.Microphone()
        except:
            pass

        if initialize_message:
            print("COMPLETED")

    def listen_for_awake(self):
        global stop_listener, is_awake

        is_awake = False
        stop_listener = self._recognizer.listen_in_background(self._microphone, listen_awake_callback)
        
        while not is_awake:
            continue
        
        return True

    def listen(self):
        try:
            with self._microphone as source:
                print("User: ", end="")
                audio = self._recognizer.listen(source)
                text = self._recognizer.recognize_google(audio)
                console.print_user_chat(text)
                return (text, True)
        except sr.UnknownValueError:
            return ("", False)
        except sr.RequestError:
            console.print_error("No internet connection available")
            exit(0)
        except SystemExit:
            self._tts.set_speed(170)
            self._tts.speak("Terminating all activities")