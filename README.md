# 🎙️ July Voice Assistant System

July is a Python-based voice assistant that interacts with users through speech recognition and text-to-speech.  
It can perform tasks like opening applications, searching the web, fetching Wikipedia summaries, playing music, telling jokes, and even chatting with you — inspired by Tony Stark's July.

---

## 🛠 Features

- ⏰ **Greeting** based on time of day (morning, afternoon, evening)
- 🎤 **Speech recognition** using Google Speech Recognition
- 🔊 **Text-to-speech** responses with `pyttsx3`
- 📅 **Time & Date** announcements
- 📖 **Wikipedia search** with spoken summaries
- 🌐 **Open websites** (Google, YouTube, Facebook, LinkedIn)
- 🎶 **Play random music** from a specified folder
- 🖥️ **Open system applications** (Calculator, Notepad, CMD)
- 📸 **Take screenshots** and save them automatically
- 📆 **Open Google Calendar** via browser
- 😂 **Tell jokes** and respond to small talk
- 🤖 **Gemini AI integration** for conversational responses
- 📝 **Logging system** to track user commands and assistant actions
- 👋 **Exit gracefully** with a voice command

---

## 💻 Requirements

- Python **3.11** or higher
- Conda (recommended for environment management)

---

## 📦 Installation

1. **Create a virtual environment:**
   ```bash
   conda create -n July python=3.11 -y
   ```

2. **Activate the environment:**
   ```bash
   conda activate July
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ How to Run

1. Make sure you have a working microphone.
2. Set your Gemini API key in a `.env` file:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```
3. Run the assistant:
   ```bash
   python July.py
   ```

---

## 📂 Project Structure

```
July-Voice-Assistant-System/
│
├── July.py              # Main script
├── requirements.txt       # Dependencies
├── logs/                  # Log files (application.log)
├── Screenshot/            # Saved screenshots
└── README.md              # Project documentation
```

---

## ⚙️ Logging

- All assistant actions and errors are logged in `logs/application.log`.
- Example log entry:
  ```
  [ 2025-11-30 22:00:00 ] root - INFO - User requested to open Notepad.
  ```

---

## 👨‍💻 Author

**Abdullah Muhammad Bakhtiar**  
Inspired by Google Assistant

---

## 📜 License

This project is **open-source** and free to use for learning purposes.
```