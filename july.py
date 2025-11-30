import speech_recognition as sr 
import pyttsx3 
import logging 
import os 
import datetime 
import wikipedia 
import webbrowser 
import random 
import subprocess 
import google.generativeai as genai 
import pyautogui
import time
from dotenv import load_dotenv
load_dotenv()


# Logging Configuration 
LOG_DIR = "logs"
LOG_FILE_NAME = "application.log"

os.makedirs(LOG_DIR, exist_ok=True)
log_path  = os.path.join(LOG_DIR, LOG_FILE_NAME)

logging.basicConfig(
    filename = log_path,
    level = logging.INFO,
    format = "[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s"
)

# Initialize Text-to-Speech Engine
engine = pyttsx3.init("sapi5") 
engine.setProperty('rate', 150)
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[0].id)


# This is speak function
def speak(text):
    """This function converts text to voice
    Args:
        text
    returns:
        voice
    """
    print(f"July Says: {text}")
    engine.say(text)
    engine.runAndWait()


# This function recognize the speech and convert it to text 
def take_command():
    """This function takes command & recognize
    Returns:
        text as query
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        logging.info("Audio captured from microphone")

        try: 
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            print("Say that again please...")
            logging.error(f"Error recognizing audio: {e}")
            return "None"
        
        return query
    

def gemini_model_response(user_input):
    """This function gets response from Gemini model
    Args:
        prompt
    Returns:
        response from Gemini model  
    """

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    genai.configure(api_key=GEMINI_API_KEY) 
    model = genai.GenerativeModel("gemini-2.5-flash")
    prompt = f"Yout name is July. Act like a virtual assistant. Answar the provided question in short, Question {user_input}. Answer give only speaking type."
    response = model.generate_content(prompt)
    return response.text

# This function greet the user based on time of day
def greeting():
    """This function greets the user based on time of day
    """

    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak("Good Morning, Sir. How are you doing?")
    elif hour < 18:
        speak("Good Afternoon, Sir. How can I assist you?")
    else:
        speak("Good Evening, Sir. Hope you had a great day!")

    speak("I am July. Please tell me how may I help you today?")




# Main Function
greeting()

while True:
    query = ""
    query = take_command().lower()
    print(f"Command received: {query}")

    if "your name" in query:
        speak("My name is July, How can I help you?.")
        logging.info("Responded to name inquiry")
    
    elif "time" in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {strTime}")
        logging.info("Provided current time")

    elif "wikipedia" in query:
        speak("Searching Wikipedia...")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        speak(results)
        logging.info("User requested information from Wikipedia.")

    elif "open youtube" in query:
        speak("Opening YouTube for you.")
        query = query.replace("open youtube", "")
        webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
        logging.info("Opened YouTube in web browser")


    elif "open google" in query:
        speak("Opening Google for you.")
        query = query.replace("google", "")
        webbrowser.open(f"https://www.google.com/search?q={query}")
        logging.info("Opened Google in web browser")

    elif "open linkedin" in query:
        speak("Opening LinkedIn for you.")
        query = query.replace("open linkedin", "")  
        webbrowser.open(f"https://www.linkedin.com/in/{query}")
        logging.info("Opened LinkedIn profile in web browser")

    elif "screenshot" in query:
        speak("Taking a screenshot for you.")
        screenshot = pyautogui.screenshot()
        LOG_DIR = "Screenshot"
        os.makedirs(LOG_DIR, exist_ok=True)
        screenshot_path = os.path.join(LOG_DIR, "screenshot.png")
        screenshot.save(screenshot_path)
        speak(f"Screenshot taken and saved at {screenshot_path}")
        logging.info("Screenshot taken and saved")

    elif "open notepad" in query:
        speak("Opening Notepad for you.")
        subprocess.Popen("notepad.exe")
        time.sleep(1)
        logging.info("User requested to open Notepad and type query.")
        pyautogui.typewrite(query)


        # while True:
        #     note = take_command().lower()
        #     pyautogui.typewrite(note)
        #     if "stop" in note:
        #         break 

        

    elif "exit" in query:
        speak("Goodbye, Sir. Have a great day!")
        logging.info("Exiting the program as per user command")
        break
    

    else: 
        speak("Thinking...")
        response = gemini_model_response(query)
        speak(response)
        logging.info("Provided response from Gemini model") 


