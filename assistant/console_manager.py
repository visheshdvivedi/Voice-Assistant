from datetime import datetime
from colorama import Fore, Style, just_fix_windows_console
just_fix_windows_console()

class ConsoleManager:

    # Severity classification
    INFO = 0
    WARN = 1
    ERR = 2

    @staticmethod
    def print_info(message, same_line=False):
        if same_line:
            print("[" + Fore.CYAN + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + Style.RESET_ALL + "][" + Fore.GREEN + "INFO" + Style.RESET_ALL + "] " + message, end="", flush=True)
        else:
            print("[" + Fore.CYAN + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + Style.RESET_ALL + "][" + Fore.GREEN + "INFO" + Style.RESET_ALL + "] " + message, flush=True)

    @staticmethod
    def print_warning(message):
        print("[" + Fore.CYAN + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + Style.RESET_ALL + "][" + Fore.YELLOW + "WARNING" + Style.RESET_ALL + "] " + message, flush=True)

    @staticmethod
    def print_error(message):
        print("[" + Fore.CYAN + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + Style.RESET_ALL + "][" + Fore.LIGHTRED_EX + "ERROR" + Style.RESET_ALL + "] " + message, flush=True)

    @staticmethod
    def print_user_chat(message):
        print("[" + Fore.CYAN + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + Style.RESET_ALL + "][" + Fore.MAGENTA + "USER" + Style.RESET_ALL + "] " + message, flush=True)

    @staticmethod
    def print_bot_chat(message):
        print("[" + Fore.CYAN + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + Style.RESET_ALL + "][" + Fore.MAGENTA + "BOT" + Style.RESET_ALL + "] " + Fore.GREEN + message + Style.RESET_ALL, flush=True)

    @staticmethod
    def get_user_input():
        try:    
            text = input("[" + Fore.CYAN + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + Style.RESET_ALL + "][" + Fore.MAGENTA + "USER" + Style.RESET_ALL + "]: ")
            return text
        except:
            return False