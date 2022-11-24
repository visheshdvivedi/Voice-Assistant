import os, json
import random
import threading
from importlib import import_module
from assistant.console_manager import ConsoleManager as console

COMMANDS_FOLDER_PATH = "assistant\\commands"
METHODS_FOLDER_PATH = "assistant\\methods"

class CommandManager:
    def __init__(self):
        self._commands = []
        self._methods = {}

        console.print_info("Reading commands...COMPLETED")

        self._read_commands()
        self._read_methods()

    def _parse_command_file(self, filename:str, filepath:str):

        if not os.path.exists(filepath):
            console.print_error(f"File path '{filepath}' does not exist")
            exit(0)

        if not filename.endswith(".json"):
            console.print_error(f"Command file '{filename}' should be a JSON file")
            exit(0)

        content = {}
        try:
            with open(filepath, 'r') as file:
                content = json.loads(file.read())
        except:
            console.print_error(f"Contents of command file '{filepath}' are not in valid JSON format")

        self._commands.append(content)

    def _parse_method_file(self, filename, filepath):

        if not os.path.exists(filepath):
            console.print_error(f"File path '{filepath}' does not exist")
            exit(0)

        if not filename.endswith(".py"):
            console.print_warning(f"Skipping file/folder '{filename}'")
            return 

        try:
            self._methods[filename.replace(".py", "")] = import_module(".".join(filepath.replace(".py", "").split("\\")))
        except Exception as ex:
            print(ex)
            console.print_error(f"Unable to import method module '{filename}'")

    def _read_commands(self):
        
        if not os.path.exists(COMMANDS_FOLDER_PATH):
            console.print_error(f"File path '{COMMANDS_FOLDER_PATH}' does not exist")
            exit(0)
        
        for file in os.listdir(COMMANDS_FOLDER_PATH):
            self._parse_command_file(file, os.path.join(COMMANDS_FOLDER_PATH, file))

    def _read_methods(self):
        
        if not os.path.exists(METHODS_FOLDER_PATH):
            console.print_error(f"File path '{METHODS_FOLDER_PATH}' does not exist")
            exit(0)
        
        for file in os.listdir(METHODS_FOLDER_PATH):
            self._parse_method_file(file, os.path.join(METHODS_FOLDER_PATH, file))

    def process_command(self, command):
        
        command_recommendation = {}
        best_score = 0
        variable_value = ""
        words = command.split(" ")
        
        for existing_command in self._commands:
            syntax = existing_command['syntax']
            left_index = syntax.rfind('{')
            right_index = syntax.rfind('}')
            
            syntax_words = (syntax[:left_index - 1] + syntax[right_index+1:]).split(" ")
            
            temp_command = command.split(" ")
            command_score = 0
            for word in syntax_words:
                for check_word in words:
                    if word == check_word:
                        command_score += 1
                        temp_command.remove(word)
            
            if command_score > best_score:
                command_recommendation = existing_command
                best_score = command_score
                variable_value = " ".join(temp_command)

        if command_recommendation != {}:
            response = random.choice(command_recommendation['response'])
            if command_recommendation['variable'] in response:
                response = response.replace(command_recommendation['variable'], variable_value)
            return response, command_recommendation, variable_value

    def perform_command_action(self, command_recommendation, variable_value):
        self._methods[command_recommendation['function']].main(variable_value)