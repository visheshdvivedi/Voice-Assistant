import os, json
from assistant.console_manager import ConsoleManager as console

BOT_CONFIG_FILEPATH = "assistant/config/botconfig.json"

class ConfigurationManager:
    def __init__(self, initialize_message=True):
        self._config = {}
        self._initialize_message = initialize_message

        if initialize_message:
            console.print_info("Reading cofigurations...", True)
            print("COMPLETED")
        
        self._read_configurations()

    def _read_configurations(self):

        if not os.path.exists(BOT_CONFIG_FILEPATH):
            console.print_error(f"Filepath '{BOT_CONFIG_FILEPATH}' does not exist")
            exit(0)

        with open(BOT_CONFIG_FILEPATH, "r") as file:
            self._config = json.loads(file.read())

        if self._initialize_message:
            console.print_info(f"Input mode: {self._config['input_mode']}")
            console.print_info(f"Voice: {self._config['voice_gender']}")

    def get_input_mode(self):
        return self._config['input_mode']

    def get_voice(self):
        return self._config['voice_gender']