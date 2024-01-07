from datetime import datetime
import pyttsx3
import joblib
import json
import webbrowser
import time
import pyautogui
import requests
import os
import subprocess
import speech_recognition as sr
import sys
import locale

engine = pyttsx3.init()
locale.setlocale(locale.LC_TIME, 'tr_TR.UTF-8')
def log(message):
    current_time = datetime.now().strftime("%H:%M:%S")
    log_message = f"[{current_time}] {message}"
    print(log_message)

def speak(audiostring):
    log(audiostring)
    engine.say(audiostring)
    engine.runAndWait()

def classify(command):
    model = joblib.load("Models\svcmodel.pkl")
    vectorizer = joblib.load("Models\svmvectorizer.pkl")

    vector = vectorizer.transform([command])
    category = model.predict(vector)
    return category

def listen():
    text = ""
    r = sr.Recognizer()
    with sr.Microphone() as source:                # use the default microphone as the audio source
        r.adjust_for_ambient_noise(source, duration=0.2) #adjust the energy threshold based on the surrounding noise level
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language='tr-TR')
            text = text.lower()
            log(text)
            if text == "kapan":
                sys.exit()
            elif text == "teşekkürler":
                speak("rica ederim")
        except LookupError:                            # speech is unintelligible
            log("Tekrar söyler misiniz")
            return listen()
        except sr.UnknownValueError:
            log("Bilinmeyen Hata")
            return listen()
    return text

def do_actions(category,command):
    if command == "özel gün ekle":
        Date.append_special_days()
        return
    if "topla" == command:
        Calculation.calculate("topla")
        return
    elif "çıkar" == command:
        Calculation.calculate("çıkar")
        return
    elif "böl" == command:
        Calculation.calculate("böl")
        return
    elif "çarp" == command:
        Calculation.calculate("çarp")
        return
        
    if category == 0:
        kontrol_listesi = ["oynat", "çal", "aç"]
        if any(substring in command for substring in kontrol_listesi):
            Music.play_music(command)
            return
    elif category == 1:
        Weather.weather_info()
        return
    elif category == 2:
        if "bugünün tarihi" in command:
            Date.current_date()
            return
        elif "hangi gün" in command:
            Date.current_day()
            return
        elif "hangi ay" in command:
            Date.current_month()
            return
        elif "hangi yıl" in command:
            Date.current_year()
            return  
        else:
            Date.special_days()
            return
    elif category == 3:
        if "program ekle" in command:
            Programs.append_program_info()
            return
        if "aç" or "başlat" in command:
            Programs.open()
            return
        elif "kapat" or "sonlandır" in command:
            Programs.close()
            return
       
class Json ():
    def __init__(self, name):
        self.name = name
        self.functions = {"write_json","load_json","append_json"}

    def write_json(data, json_path):
        with open(json_path, 'w', encoding="utf-8") as json_file:
                json.dump(data, json_file, ensure_ascii=False)

    def load_json(json_path):
        with open(json_path, 'r', encoding="utf-8") as json_file:
            return json.load(json_file)
    
    def append_json(data, json_path):
        loaded_data = Json.load_json(json_path)
        loaded_data.append(data)
        Json.write_json(loaded_data,json_path)

class Music():
    def __init__(self, name):
        self.name = name
        self.functions = {"play_music"}

    def play_music(command):
        base_url = "https://www.youtube.com/results?search_query=" + command
        webbrowser.open(base_url)
        time.sleep(5)
        pyautogui.click(560, 324)
        time.sleep(10)
        log("Şarkı oynatılıyor")

class Weather():
    def __init__(self, name):
        self.name = name
        self.functions = {"weather_info"}
    
    def weather_info():
        country = ''
        speak("Şehir bilgisini tekrar edebilir misiniz")
        city = listen()
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
        else:
            speak("enlem boylam tespit edilemedi")

        weather_base_url = 'https://api.openweathermap.org/data/2.5/weather?'

        weather_params = {
        'lat': lat,
        'lon': lon,
        'appid': "1d47169fd917e33f11df6c1fb2d67f84",
        'units': 'metric', 
        'lang': 'tr'
        }
        
        # Make the API request
        weather_response = requests.get(weather_base_url, params=weather_params)
        weather_data = weather_response.json()

        # Check if the request was successful
        if weather_response.status_code == 200:
            # Extract relevant weather information
            description = weather_data['weather'][0]['description']
            temperature = weather_data['main']['temp']
            humidity = weather_data['main']['humidity']

            # Print or return the weather information
            result = f'{city} şehrindeki havadurumu {description}. '
            result += f'Sıcaklık: {temperature} Derece Nem: Yüzde {humidity}'
            speak(result)
        else :
            speak("Hava durumu verisi alınırken bir sorun ile karşılaşıldı")

class Date():
    def __init__(self, name):
        self.name = name
        self.functions = {"current_day", "current_month" , "current_year", "current_date",  "special_days", "append_special_days"}

    def current_day():
        current_day = datetime.now().strftime('%A')
        speak("Bugün günlerden " + current_day)

    def current_month():
        current_month = datetime.now().strftime('%B')
        speak(current_month + " ayındayız")

    def current_year():
        current_year = datetime.now().strftime('%Y')
        speak(current_year + " yılındayız")

    def current_date():
        current_date = datetime.now().strftime('"%d %B %Y"')
        speak("Bugünün tarihi " + current_date)
    
    def special_days():
        special_days = Json.load_json("Json\special_day_data.json")
        speak("Özel günü tekrar söyleyebilir misiniz")
        day_name = listen()
        for key in special_days:
            if day_name in key["day_name"]:
                event_date = key["datetime"]
                speak( day_name + " tarihi "+ event_date)

    def append_special_days():
        speak("Özel günün adı ne olsun")
        day_name = listen()
        speak("Özel günün tarihini söyler misiniz")
        day_date = listen()
        data = {"day_name": day_name, "datetime": day_date}
        Json.write_json(data,"Json\special_day_data.json")
        speak("Özel gün eklendi")
    
class Programs():
    def __init__(self, name):
        self.name = name
        self.functions = {"open", "close","append_program_info"}

    def open():
        speak("açmamı istediğiniz programın adını söyler misiniz")
        program_name = listen()
        json_file = Json.load_json("Json\program_data.json")

        for program_data in json_file:
            print(program_data)
            if program_data['program_name'] == program_name:
                 program_path = program_data['path']
                 os.startfile(program_path)
                 speak(program_name + "açıldı")
                 break

    def close():
        speak("kapatmamı istediğiniz programın adını söyler misiniz")
        program_name = listen()
    
        result = subprocess.run(['tasklist'], stdout=subprocess.PIPE, text=True)
        json_file = Json.load_json("Json\program_data.json")
        for data in json_file:
            if data['program_name'] == program_name:
                 exe_name = data['exe_name']
                 speak(program_name + "kapatıldı")
                 break
        # Check if the program name is in the command output
        if program_name.lower() in result.stdout.lower():
            # Terminate the process
            os.system(f'taskkill /im {exe_name}.exe /f')
            print(f"Closed {program_name} successfully.")
        else:
            print(f"Program {program_name} not found.")

    def append_program_info(program_name,path,exe_name):
        speak("program adını giriniz")
        program_name = input()
        speak("programın yolunu giriniz")
        path = input()
        speak("program exe adını giriniz")
        exe_name = input()
        data = {"program_name": program_name, "path": path, "exe_name": exe_name}
        Json.append_json(data,"Json\program_data.json")
        speak("program eklendi")

class Calculation():
    def __init__(self, name):
        self.name = name
        self.functions = {"get_numbers","calculate"}
    
    def get_numbers():
        numbers = []
        speak("ilk numarayı söyleyin")
        num1 = listen()
        numbers.append(num1)
        speak("ikinci numarayı söyleyin")
        num2 = listen()
        numbers.append(num2)
        return numbers
       
    def calculate(process):
        numbers = []
        numbers = Calculation.get_numbers()
        if process == "topla":
            result = int(numbers[0]) + int(numbers[1])
            speak("Cevap " + str(result))
            return
        elif process == "çıkar":
            if int(numbers[0]) < int(numbers[1]):
                result = int(numbers[1]) - int(numbers[0])
            else:
                result = int(numbers[0]) - int(numbers[1])
            speak("Cevap " + str(result))
            return
        elif process == "çarp":
            result = int(numbers[0]) * int(numbers[1])
            speak("Cevap " + str(result))
            return 
        elif process == "böl":
            if int(numbers[0]) < int(numbers[1]):
                result = int(numbers[1]) / int(numbers[0])
            else:
                result = int(numbers[0]) / int(numbers[1])
            speak("Cevap " + str(result))
            return
        

