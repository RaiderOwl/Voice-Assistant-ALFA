#Libraries
import speech_recognition as sr
from datetime import datetime
from gtts import gTTS
import sys
import joblib
import pyttsx3
import pandas as pd
import numpy as np
import webbrowser
import pywhatkit as kt
import webbrowser as wb
import time
import pyautogui
import keyboard
import sounddevice as sd
import requests
import threading
import subprocess
import os 
import psutil
import json
#Functions
def log(message):
    current_time = datetime.now().strftime("%H:%M:%S")
    log_message = f"[{current_time}] {message}"
    print(log_message)

def listen():
    text = ""
    r = sr.Recognizer()
    with sr.Microphone() as source:                # use the default microphone as the audio source
        r.adjust_for_ambient_noise(source, duration=0.2) #adjust the energy threshold based on the surrounding noise level
        speak("sizi dinliyorum")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language='tr-TR')
            text = text.lower()
            log(text)
            if text == "kapan":
                sys.exit()
        except LookupError:                            # speech is unintelligible
            log("Tekrar söyler misiniz")
            return listen()
        except sr.UnknownValueError:
            log("Bilinmeyen Hata")
            return listen()
    return text

def speak(audiostring):
    log(audiostring)
    engine.say(audiostring)
    engine.runAndWait()

def classify(command):
    speak("İşleme Alındı")
    model = joblib.load("newsvcmodel.pkl")
    vectorizer = joblib.load("newsvmvectorizer.pkl")

    command_vector = vectorizer.transform([command])
    category = model.predict(command_vector)
    print(category)
    return category

def do_actions(category, response):
    speak(Calculation.calculate(response))

class Json ():
    def __init__(self, name):
        self.name = name
        self.functions = {}

    def write_json(data, json_path):
        with open(json_path, 'w') as json_file:
                json.dump(data, json_file)

    def load_json(json_path):
        with open(json_path, 'r') as json_file:
            return json.load(json_file)
    
    def append_json(data, json_path):
        loaded_data = Json.load_json(json_path)
        loaded_data.append(data)
        Json.write_json(loaded_data,json_path)

class Music():
    def __init__(self, name):
        self.name = name
        self.functions = {}

    def play_music(song_name):
        base_url = "https://www.youtube.com/results?search_query=" + song_name
        webbrowser.open(base_url)
        time.sleep(5)
        pyautogui.click(560, 324)
        time.sleep(10)

class Weather():
    def __init__(self, name):
        self.name = name
        self.functions = {}
    
    def weather_info(city, country=''):
        geocode_base__url = 'https://api.opencagedata.com/geocode/v1/json?'

        geocode_params = {
            'q': f'{city},{country}',
            'key': "48a3fe66d9ab40e8a0a7210620ace1fa"
        }

        geocode_response = requests.get(geocode_base__url, params=geocode_params)
        geocode_data = geocode_response.json()

        if geocode_response.status_code == 200:
            # Extract latitude and longitude
            lat = geocode_data['results'][0]['geometry']['lat']
            lon = geocode_data['results'][0]['geometry']['lng']
            print(lat)
            print(lon)
        weather_base_url = 'https://api.openweathermap.org/data/2.5/weather?'

        weather_params = {
        'lat': lat,
        'lon': lon,
        'appid': "1d47169fd917e33f11df6c1fb2d67f84",
        'units': 'metric'  # You can change this to 'imperial' for Fahrenheit
        }
        

        # Make the API request
        weather_response = requests.get(weather_base_url, params=weather_params)
        weather_data = weather_response.json()
        print(weather_data)
        # Check if the request was successful
        if weather_response.status_code == 200:
            # Extract relevant weather information
            description = weather_data['weather'][0]['description']
            temperature = weather_data['main']['temp']
            humidity = weather_data['main']['humidity']

            # Print or return the weather information
            result = f'The weather in {city} is {description}. '
            result += f'Temperature: {temperature}°C. Humidity: {humidity}%.'
            print(result)

class Date():
    def __init__(self, name):
        self.name = name
        self.functions = {}

    def today():
        # Get the current date and format it
        current_date = datetime.now().strftime('%Y-%m-%d')
        return current_date
    
    def special_days(day_name):
        special_days = {
            "yılbaşı": "1 ocak",
            "ulusal egemenlik ve çocuk bayramı": "23 nisan",
            "emek ve dayanışma günü": "1 mayıs",
            "atatürk'ü anma, gençlik ve spor bayramı": "19 mayıs",
            "zafer bayramı": "30 ağustos",
            "cumhuriyet bayramı": "29 ekim",
            "öğretmenler günü": "24 kasım",
            "sevgililer günü": "14 şubat",
            "dünya kadınlar günü": "8 mart",
            "çanakkale zaferi": "18 mart",
            "demokrasi ve milli birlik günü": "15 temmuz"
        }
        for key in special_days:
            if day_name.lower() in key.lower():
                event_date = special_days[key]
                print(event_date)
                return event_date

class Time():
    def __init__(self, name):
        self.name = name
        self.functions = {}
    
    def now():
        current_time = datetime.now().strftime("%H:%M:%S")
        return current_time
    
    def alarm(hour,minutes):
        alarm_hour = hour
        alarm_minute = minutes
        alarm = 1
        temp_time = Time.now()
        while alarm == 1 and temp_time.second == "01":
            current_time = datetime.now().strftime("%H:%M:%S")
            if current_time.hour == alarm_hour and current_time.minute == alarm_minute:
                speak("Alarm. Uyanın")
                break
            else:
                time.sleep(60)  # Check every 60 seconds

    def timer_callback():
        speak("zaman doldu")

    def timer(minutes=None, seconds=None):

        duration_seconds = (minutes or 0) * 60 + (seconds or 0)
        timer = threading.Timer(duration_seconds, Time.timer_callback)
        timer.start()
        
class Programs():
    def __init__(self, name):
        self.name = name
        self.functions = {}

    def open(program_name):
        json_file = Json.load_json("program_data.json")

        for program_data in json_file:
            print(program_data)
            if program_data['program_name'] == program_name:
                 program_path = program_data['path']
                 os.startfile(program_path)
                 break

    def close(program_name):
        # Run the tasklist command to get a list of processes
        result = subprocess.run(['tasklist'], stdout=subprocess.PIPE, text=True)
        json_file = Json.load_json("program_data.json")
        for data in json_file:
            if data['program_name'] == program_name:
                 exe_name = data['exe_name']
                 break
        # Check if the program name is in the command output
        if program_name.lower() in result.stdout.lower():
            # Terminate the process
            os.system(f'taskkill /im {exe_name}.exe /f')
            print(f"Closed {program_name} successfully.")
        else:
            print(f"Program {program_name} not found.")

    def append_program_info(program_name,path,exe_name):
        data = {"program_name": program_name, "path": path, "exe_name": exe_name}
        Json.append_json(data,"program_data.json")

class Calculation():
    def __init__(self, name):
        self.name = name
        self.functions = {}
    
    def get_numbers():
        numbers = []
        speak("işlem yapılacak ilk numarayı söyleyin")
        num1 = listen()
        numbers.append(num1)
        speak("işlem yapılacak ikinci numarayı söyleyin")
        num2 = listen()
        numbers.append(num2)
        return numbers
    
    def add(numbers):
        return int(numbers[0]) + int(numbers[1])
    
    def subtract(numbers):
        return int(numbers[0]) - int(numbers[1])
    
    def multiple(numbers):
        return int(numbers[0]) * int(numbers[1])
    
    def divide(numbers):
        if int(numbers[0]) < int(numbers[1]):
            return int(numbers[1]) / int(numbers[0])
        else:
            return int(numbers[0]) / int(numbers[1])
        
    def calculate(process):
        numbers = []
        numbers = Calculation.get_numbers()
        if process == "topla":
            return Calculation.add(numbers)
        elif process == "çıkar":
            return Calculation.subtract(numbers)
        elif process == "çarp":
            return Calculation.multiple(numbers)
        elif process == "böl":
            return Calculation.divide(numbers)

# def do_actions(category):
#     function_mapping = {
#         1: function_1,  # Kategori 1 için fonksiyon
#         2: function_2,  # Kategori 2 için fonksiyon
#         3: function_3,  # Kategori 3 için fonksiyon
#         4: function_4,  # Kategori 4 için fonksiyon
#         5: function_5,  # Kategori 5 için fonksiyon
#         6: function_6,  # Kategori 6 için fonksiyon
#     }
#     function_mapping[category]()

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

welcometext = "Merhaba Ben alfa"
speak(welcometext)

while True:
    response = listen()
    category = classify(response)
    do_actions(category, response)



