🔹 Keylogger & Mouse Tracker

This is a basic keylogger and mouse activity tracker built using Python, Tkinter, and Pynput. I developed this project a long time ago as a simple way to understand how a keylogger works. Over time, I improved it by adding mouse tracking, timestamps, and a GUI to start/stop logging.

📌 Features

✅ Records keystrokes (pressed & released keys)✅ Tracks mouse movements, clicks, and scrolls✅ Saves logs in logs.txt (plain text) & logs.json (structured JSON)✅ Timestamps every event (keystrokes & mouse activity)✅ Tkinter GUI to start/stop logging & clear logs✅ Does NOT close on stop (so logs can be cleared before exiting)

📂 Log File Formats

1️⃣ logs.txt (Plain Text Format)

a b c ENTER SHIFT d e f

2️⃣ logs.json (Structured Format)

{
    "keys": [
        {"Pressed": "a", "Timestamp": "2025-03-22 14:05:10"},
        {"Released": "a", "Timestamp": "2025-03-22 14:05:11"},
        {"Pressed": "b", "Timestamp": "2025-03-22 14:05:12"}
    ],
    "mouse": [
        {"Move": "(200, 450)", "Timestamp": "2025-03-22 14:05:15"},
        {"Clicked": "Left at (220, 460)", "Timestamp": "2025-03-22 14:05:16"}
    ]
}

🛠️ Setup & Usage

1️⃣ Install Dependencies

pip install pynput

2️⃣ Run the Program

python keylogger.py

3️⃣ Use the GUI

🟢 Start Logging → Begins tracking keystrokes & mouse movement

🔴 Stop Logging → Stops logging (but keeps window open)

🧹 Clear Logs → Deletes all stored logs

⚠️ Disclaimer

This project is for educational purposes only. Do NOT use this tool for any illegal activity. Unauthorized keylogging is illegal and unethical. Always get consent before running a keylogger on any device.

📌 Future Improvements

🔹 Add an option to email logs automatically 📧🔹 Implement stealth mode (run in background) 👀🔹 Export logs in CSV format 📚

🔹 Developed by Katherine OliviaA basic project from the past, just for learning purposes! 🚀