import random
import json
import pandas as pd
def generate_sentences(artist_names, song_names, verb_names, num_sentences):
    generated_sentences = []

    for _ in range(num_sentences):
        artist = random.choice(artist_names)
        song = random.choice(song_names)
        verb = random.choice(verb_names)

        generated_sentence =artist + " " + song + " " + verb
        generated_sentences.append(generated_sentence)

    return generated_sentences

# Kullanıcı tarafından belirlenecek özellikler
artist_names = [
    "Ebru Gündeş", "Tarkan", "Sezen Aksu", "Sertab Erener", "Teoman",
    "Hande Yener", "Kenan Doğulu", "Ajda Pekkan", "Cem Adrian", "Şebnem Ferah",
    "Barış Manço", "Nilüfer", "Mor ve Ötesi", "Yalın",
    "Müslüm Gürses", "İbrahim Tatlıses",  "Candan Erçetin", "Yüksek Sadakat",
    "Gripin", "Athena", "Yıldız Tilbe", "Mor ve Ötesi","Duman",  "Cem Karaca", "Hayko Cepkin","Altay","Aşkın Nur Yengi","Atiye","Bengü","Bedük","Berkay","Demet Akalın","Emre Altuğ","Ferhat Göçer","Gökçe","Gökhan Türkmen",
    "Göksel","Hadise","Gülsen","Simge Sağın","İrem Derici","Merve Özbey","Murat Boz","Sibel Can","Murat Dalkılıç","Mustafa Ceceli","Nil Karaibrahimgil","Serdar Ortaç",
    "Yalın","Ziynet Sali"
]

song_names = [
    "Abidik Gubidik Twist","Acem Kızı","Ada Sahillerinde Bekliyorum","Adem Olan Anlar","Adını Anmam","Ağlama Yar Ağlama","Ağrı Dağından Aştım",
    "Ah Bir Ataş Ver","Akdeniz Akşamları","Aman Aman Nalbandım","Anası Kızından","Ankara Rüzgarı","Ankara'dan Abim Geldi","Ankara'nın Taşına Bak (Ankara türküsü)","Arım, Balım, Peteğim (şarkı)",
    "Asmalı Mencere",
    "Aşk Sakızı",
    "Ayağında Kundura",
    "Aysel Gürel tarafından yazılmış şarkılar listesi",
    "Ayva Çiçek Açmış",
    "Bafra oyun havası",
    "Bak Bir Varmış Bir Yokmuş",
    "Balad (albüm)",
    "Bastım da Kırıldı İğdenin Dalı",
    "Bedia...",
    "Bekle Buğday Tanesi",
    "Beklenen Şarkı (şarkı)",
    "Ben Kalender Meşrebim Güzel Çirkin Aramam",
    "Benzemez Kimse Sana",
    "Bıçak Düşmez Belinden",
    "Bir Dalda İki Kiraz",
    "Bir İncecik Yolum Gider Gördes'e",
    "Bir Of Çeksem Karşıki Dağlar Yıkılır (Kar Mı Yağmış)",
    "Böyle Ayrılık Olmaz",
    "Böyle Gelmiş Böyle Geçer Dünya",
    "Bu Kalp Seni Unutur Mu",
    "Cano Cano Cano",
    "Cumartesi Türküsü",
    "Çadırımın Üstüne",
    "Çok Yaşa Sen Ayşe",
    "Dağlarda Kar Olsaydım",
    "Daha Senden Gayrı Aşık mı Yoktur",
    "Dandini Dandini Dastana",
    "Darıldın Mı Gülüm Bana",
    "Der makam-ı Hüseyni Sakil-i Ağa Rıza",
    "Der makam-ı Şüri Sema'i",
    "Dillere Düşeceğiz Seninle",
    "Dinle (Şebnem Paker albümü)",
    "Dom Dom Kurşunu",
    "Dört Peynirli Pizza (Hepsi şarkısı)",
    "El Çek Tabip Sinem Üstünden",
    "Elazığ Dik Halayı",
    "Elbet Bir Gün Buluşacağız",
    "Entarisi Ala Benziyor",
    "Erkekler (şarkı)",
    "Eşkıya Dünyaya Hükümdar Olmaz",
    "Ezberbozan",
    "Geçsin Günler, Haftalar, Aylar, Mevsimler, Yıllar",
    "Gel Ayşem Gel Gezelim",
    "Gel, Sen de Katıl Umudun Şarkısına!",
    "Gemilerde Talim Var",
    "Genç Osman Türküsü",
    "Gözlerinin İçine Başka Hayal Girmesin",
    "Gözünaydın",
    "Hatırla Sevgili (şarkı)",
    "Hava Nasıl Oralarda  (şarkı)",
    "Hekimoğlu Derler Benim Aslıma",
    "Hepsi Senin mi ",
    "Her Şeye Rağmen (şarkı)",
    "Hey Onbeşli",
    "Hüp",
    "İndim Havuz Başına",
    "İzmir’in Kavakları",
    "Kadifeden Kesesi",
    "Kalbime Gömerim O Zaman",
    "Kalpsizsin",
    "Karam (Köprüler Yaptırdım Gelip Geçmeye)",
    "Kâtibim",
    "Katina'nın elinde makina",
    "Keklik Gibi Kanadımı Süzmedim",
    "Kız Çocuğu (şiir)",
    "Kızılcıklar Oldu mu ",
    "Kimseye Etmem Şikâyet",
    "Kirlenmiş Çığlık",
    "Konyalım",
    "Küçük Ayşe (Küçük Asker)",
    "Küçük Yaşta Aldım Sazı Elime",
    "Mahur (şiir)",
    "Mahur Peşrev (Gazi Giray Han)",
    "Maraş'tan Bir Haber Geldi",
    "Mavilim Uyanda Gel",
    "Memleketim (şarkı)",
    "Mendilim Allanıyor",
    "Mendilimin Yeşili",
    "Meşe Şarkısı",
    "Müzik plakları dolduran Türk sinema oyuncuları",
    "Ne Feryad Edersin Divane Bülbül",
    "Nerden Gelirsin (Keklik)",
    "O Şimdi Asker (şarkı)",
    "On İkidir Aydın'ın Dermeni",
    "Ormandan Gel",
    "Ömrümce hep adım adım",
    "Önsöz (şarkı)",
    "Ramizem",
    "Sabahın Seher Vaktinde",
    "Saçları Kara Kız Kız (Podaraki)",
    "Sana Güvenmiyorum (şarkı)",
    "Sana Neler Edeceğim",
    "Sarı Odalar",
    "Sarı Saçlım Mavi Gözlüm",
    "Sarı Zeybek",
    "Sen beni unutmuşsun (Sakın dönme geriye)",
    "Sen Bir Tanesin",
    "Senden Ayrı Aylar Geçti Yıl Geçti (Dağlar)",
    "Sevda Mıdır Yoksa",
    "Sıra Sıra Siniler (Çanakkale türküsü)",
    "Son Mektup (şarkı)",
    "Şimdi Uzaklardasın",
    "Şu Dağları Delmeli",
    "Şu Gelen Atlı Mıdır (Damdan Düştüm Dalgalanıyorum)",
    "Talihin Elinde Oyuncak Oldum",
    "Tarkan Çakır - Z.A.C.",
    "Tarkan Çakır (albüm)",
    "Telgrafın Tellerine Kuşlar Mı Konar",
    "Toz Pembe",
    "Turna (türkü)",
    "Türkiyem (şarkı)",
    "Uçun Kuşlar Uçun İzmir'e Doğru",
    "Uyan Sunam Uyan",
    "Üç Kalp",
    "Var Git Turnam",
    "Vücud İkliminin Sultanı Sensin",
    "Yallah Şoför",
    "Yandım Tokat Yandım",
    "Yaşasın Okulumuz",
    "Yemen Türküsü",
    "Yeni (şarkı)",
    "Yolun Başı",
    "Zeytinyağlı Yiyemem Aman",
    "Zor Kadın"
]

verb_names = ["oynat","çal","aç"]

# Toplamda kaç cümle oluşturmak istediğinizi belirleyin
num_generated_sentences = 800

# Cümleleri oluştur
generated_sentences_for_music = generate_sentences(artist_names, song_names, verb_names, num_generated_sentences)

# Oluşturulan cümleleri yazdır
# for i, sentence in enumerate(generated_sentences_for_music, start=1):
#     print(f"{i}. {sentence}")

cities = [
    "Adana", "Adıyaman", "Afyonkarahisar", "Ağrı", "Amasya",
    "Ankara", "Antalya", "Artvin", "Aydın", "Balıkesir",
    "Bilecik", "Bingöl", "Bitlis", "Bolu", "Burdur",
    "Bursa", "Çanakkale", "Çankırı", "Çorum", "Denizli",
    "Diyarbakır", "Edirne", "Elazığ", "Erzincan", "Erzurum",
    "Eskişehir", "Gaziantep", "Giresun", "Gümüşhane", "Hakkari",
    "Hatay", "Isparta", "İçel (Mersin)", "İstanbul", "İzmir",
    "Kars", "Kastamonu", "Kayseri", "Kırklareli", "Kırşehir",
    "Kocaeli", "Konya", "Kütahya", "Malatya", "Manisa",
    "Kahramanmaraş", "Mardin", "Muğla", "Muş", "Nevşehir",
    "Niğde", "Ordu", "Rize", "Sakarya", "Samsun",
    "Siirt", "Sinop", "Sivas", "Tekirdağ", "Tokat",
    "Trabzon", "Tunceli", "Şanlıurfa", "Uşak", "Van",
    "Yozgat", "Zonguldak", "Aksaray", "Bayburt", "Karaman",
    "Kırıkkale", "Batman", "Şırnak", "Bartın", "Ardahan",
    "Iğdır", "Yalova", "Karabük", "Kilis", "Osmaniye", "Düzce"
]

weather_question_templates = [
    "Hava durumu nasıl şehir ismi",
    "Şu anki hava durumu nedir şehir ismi",
    "şehir ismi hava nasıl",
    "Hava durumu tahminleri nedir şehir ismi",
    "şehir ismi hava durumu raporu nedir",
    "Bugün hava nasıl şehir ismi",
    "Yarın hava durumu ne olacak şehir ismi",
    "Hafta sonu için hava durumu tahminleri nedir şehir ismi"
]

generated_sentences_for_weather = []

for _ in range(600):
    city = random.choice(cities)
    question_template = random.choice(weather_question_templates)
    question = question_template.replace('şehir ismi', city)
    generated_sentences_for_weather.append(question)

# for i, sentence in enumerate(generated_sentences_for_weather, start=1):
#    print(f"{i}. {sentence}")

with open("special_day_data.json", 'r', encoding='utf-8') as json_file:
    special_day_data = json.load(json_file)

special_days = []

for day in special_day_data:
    special_days.append(day['day_name'])

date_question_templates = [
    "xgünü gününün tarihi nedir",
    "xgünü günü ne zaman",
    "xgünü günü"
    "yisim doğum günü tarihi nedir",
    "yisim doğum günü",
    "yisim doğum günü ne zaman",
    "yisim ne zaman doğdu"
    "xgünü hangi tarihte",
    "xgünü hangi günde kutlanır"
]

date_questions = [
    "Bugünün tarihi nedir",
    "Bugün günlerden ne",
    "Hangi aydayız",
    "Hangi gündeyiz",
    "Bugün hangi gün",
    "Yarın hangi gün ",
    "Haftada kaç gün var",
    "Sonraki ay ne",
    "Yarın günlerden nedir",
    "Yarın hangi gündü",
    "Dün hangi tarihti",
    "Dünün tarihi nedir",
    "Yarının tarihi nedir",
]

turkish_names = [
    "Ahmet", "Ayşe", "Mustafa", "Fatma", "Mehmet", "Zeynep", "Emine", "Ali", "Hüseyin", "Aysel",
    "Hasan", "Hatice", "İbrahim", "Yusuf", "Şehrazat", "Cemal", "Gülay", "Ahmetcan", "Elif", "Ömer",
    "Cemile", "Selim", "Zehra", "Murat", "Sevim", "Cem", "Selin", "Berkay", "Deniz", "Gizem",
    "Sadiye", "Okan", "Tuğba", "Onur", "Serpil", "Serkan", "Asuman", "Volkan", "Nazlı", "Bilge",
    "Halit", "Gamze", "İsmail", "Leyla", "Cihan", "Sibel", "Umut", "Gül", "Kerem", "Derya"
]

generated_sentences_for_date = []

for dates in date_questions:
    generated_sentences_for_date.append(dates)

for _ in range(500):
    question_template = random.choice(date_question_templates)

    if "xgünü" in question_template:
        day = random.choice(special_days)
        question = question_template.replace('xgünü', day)
    elif "yisim" in question_template:
        name = random.choice(turkish_names)
        question = question_template.replace('yisim', name)
    
    generated_sentences_for_date.append(question) 

# for sentence in generated_sentences_for_date:
#    print(sentence)

program_names = [
    "Word", "Excel", "PowerPoint", "Visual Studio", "Photoshop", "Illustrator", "Chrome", "Firefox",
    "Sublime Text", "PyCharm", "Eclipse", "Unity", "Android Studio", "Atom", "Notepad++", "MATLAB",
    "AutoCAD", "Blender", "VLC Media Player", "Zoom", "Teams", "Discord", "Git", "GitHub",
    "InDesign", "Premiere Pro", "After Effects", "Maya", "3ds Max", "Safari", "Edge", "IntelliJ IDEA",
    "NetBeans", "RStudio", "Xcode", "TensorFlow", "PyTorch", "Jupyter", "VS Code", "Brave", "FileZilla",
    "WinRAR", "7-Zip", "MySQL Workbench", "Postman", "Cinema 4D", "Final Cut Pro", "Logic Pro"
    # İhtiyacınıza göre program isimlerini ekleyebilirsiniz
]

program_sentence_templates = [
    "x  uygulamasını aç",
    "x  uygulamasını kapat",
    "x  uygulamasını çalıştır",
    "x  uygulamasını sonlandır",
    "x aç",
    "x kapat",
    "x çalıştır",
    "x sonlandır",
    "x programını aç",
    "x programını kapat",
    "x programını çalıştır",
    "x programını sonlandır"
    # İhtiyacınıza göre cümle şablonlarını ekleyebilirsiniz
]

generated_sentences_for_program = []

for _ in range(700):  # Artık sadece 10 cümle oluşturuyorum, sizin ihtiyacınıza göre arttırabilirsiniz
    program_name = random.choice(program_names)
    sentence_template = random.choice(program_sentence_templates)
    sentence = sentence_template.replace('x', program_name)
    generated_sentences_for_program.append(sentence)

# for sentence in generated_sentences_for_program:
#     print(sentence) 

generated_sentences_for_calculation = []

math_sentence_templates = [
    "sayi1 ile sayi2'yi topla",
    "sayi1'yi sayi2'ye ekle",
    "sayi1'yi sayi2'den çıkar",
    "sayi1 ile sayi2'yi çarp",
    "sayi1'yi sayi2'ye böl",
    "sayi1 ile sayi2'yi topla ve sonucu ekrana yaz",
    "sayi1'yi sayi2'ye ekle ve sonucu göster",
    "sayi1'yi sayi2'den çıkar ve sonucu yaz",
    "sayi1 ile sayi2'yi çarp ve sonucu göster",
    "sayi1'yi sayi2'ye böl ve sonucu yaz",
    "sayi1'yi sayi2'ye böldüğümüzde kalan nedir",
    "sayi1'yi sayi2'ye böl ve kalanı ekrana yaz",
    "sayi1'yi sayi2'ye böl ve kalanı göster",
    "sayi1'yi sayi2'ye böl ve kalanı yaz"
    # İhtiyacınıza göre cümle şablonlarını ekleyebilirsiniz
]


for _ in range(450):  # Artık sadece 10 cümle oluşturuyorum, sizin ihtiyacınıza göre arttırabilirsiniz
    x = random.randint(1, 100)
    y = random.randint(1, 100)

    sentence_template = random.choice(math_sentence_templates)
    sentence = sentence_template.replace('sayi1', str(x)).replace('sayi2', str(y))
    generated_sentences_for_calculation.append(sentence)

# Oluşturulan cümleleri ekrana yazdırma
# for sentence in generated_sentences_for_calculation:
#     print(sentence)
    
df = pd.DataFrame(columns=['sentence', 'label'])

df = pd.concat([df, pd.DataFrame({'sentence': generated_sentences_for_music, 'label': '0'})], ignore_index=True)
df = pd.concat([df, pd.DataFrame({'sentence': generated_sentences_for_weather, 'label': '1'})], ignore_index=True)
df = pd.concat([df, pd.DataFrame({'sentence': generated_sentences_for_date, 'label': '2'})], ignore_index=True)
df = pd.concat([df, pd.DataFrame({'sentence': generated_sentences_for_program, 'label': '3'})], ignore_index=True)
# df = pd.concat([df, pd.DataFrame({'sentence': generated_sentences_for_calculation, 'label': '4'})], ignore_index=True)


df = df.sample(frac=1).reset_index(drop=True)

print(df)

df.to_csv('Data\data.csv', index=False)







