import pyttsx3
import functions as func

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

welcometext = "Merhaba Ben ALFA"
func.speak(welcometext)

while True:
    command = func.listen()
    category = func.classify(command)
    func.do_actions(category,command)


