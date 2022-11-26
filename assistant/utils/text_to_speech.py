import pyttsx3
from assistant.console_manager import ConsoleManager
from assistant.configuration_manager import ConfigurationManager

MALE_VOICE_ID = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
FEMALE_VOICE_ID = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
THIRD_VOICE_ID = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0"

class TextToSpeech:
    def __init__(self, initialize_message = False):

        if initialize_message:
            ConsoleManager.print_info("Initializing text to speech drive...", True)

        self._config = ConfigurationManager(False)

        self._engine = pyttsx3.init(driverName='sapi5')
        self._engine.setProperty("rate", 150)
        self._engine.setProperty("volume", 0.5)

        if self._config.get_voice() == "male":
            self._engine.setProperty('voice', MALE_VOICE_ID)
        elif self._config.get_voice() == "female":
            self._engine.setProperty('voice', FEMALE_VOICE_ID)
        elif self._config.get_voice() == "other":
            self._engine.setProperty('voice', THIRD_VOICE_ID)

        if initialize_message:
            print("COMPLETED")

    def is_busy(self):
        return self._engine.isBusy()
    
    def set_speed(self, speed):
        self._engine.setProperty("rate", speed)

    def get_speed(self):
        return self._engine.getProperty("rate")
    
    def set_volume(self, volume):
        self._engine.setProperty("volume", volume)

    def get_volume(self):
        return self._engine.getProperty("volume")

    def speak(self, message):
        try:
            if message != "":
                ConsoleManager.print_bot_chat(message)
                self._engine.say(message)
                self._engine.runAndWait()
        except:
            ConsoleManager.print_error("Bot is unable to speak")
            exit(0)