from assistant.command_manager import CommandManager
from assistant.utils.speech_to_text import SpeechToText
from assistant.utils.text_to_speech import TextToSpeech
from assistant.console_manager import ConsoleManager as console
from assistant.configuration_manager import ConfigurationManager

class ConversationManager:
    def __init__(self):
        self._stt = SpeechToText(True)
        self._tts = TextToSpeech(True)
        self._config = ConfigurationManager()
        self._command = CommandManager()

        self._awake = False
        self._start_message()

    def _start_message(self):
        self._tts.speak("Importing preferences from home interface")
        self._tts.speak("Jarvis is now online and at your service")

    def start_conversation(self):
        try:
            while True:
                if self._config.get_input_mode() == "voice":

                    console.print_info("Jarvis is sleeping...say 'hey jarvis' to wake him up")
                    self._stt.listen_for_awake()
                    self._tts.speak("Yes sir, what can I do for you ?")
                    self._awake = True

                    while self._awake:
                        user_command, valid = self._stt.listen()
                        if not valid:
                            break
                        response, command, variable = self._command.process_command(user_command)
                        self._tts.speak(response)
                        self._command.perform_command_action(command, variable)
                        
                elif self._config.get_input_mode() == "text":
                    text = console.get_user_input()
                    if text == False:
                        raise SystemExit()
                    response, command, variable = self._command.process_command(text)
                    self._tts.speak(response)
                    self._command.perform_command_action(command, variable)

        except SystemExit:
            print()
            self._tts.set_speed(170)
            self._tts.speak("Terminating all activities")
            self._tts.speak("see you later")