import subprocess
import threading
from assistant.console_manager import ConsoleManager as console

APPS = {
    "calculator": "calc.exe",
    "notepad": "notepad.exe"
}

def run_thread(app_name):
    subprocess.call([APPS[app_name]])

def main(app_name):
    app_name = app_name.lower()
    if app_name in APPS:
        threading.Thread(target=run_thread, args = [app_name, ]).start()