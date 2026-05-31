import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import speech_recognition as sr
from deep_translator import GoogleTranslator
import random
import time

words_by_level = {
    "easy": [
        "кот", "пёс", "дом", "мяч", "рыба",
        "нос", "рот", "глаз", "рука", "нога",
        "стол", "стул", "окно", "дверь", "хлеб",
        "вода", "молоко", "сыр", "суп", "чай"
    ],
    "medium": [
        "школа", "учитель", "урок", "тетрадь", "карандаш",
        "портфель", "библиотека", "животное", "растение", "погода",
        "автобус", "магазин", "больница", "аптека", "столица",
        "путешествие", "профессия", "компьютер", "телефон", "интернет"
    ],
    "hard": [
        "технология", "университет", "информация", "произношение", "воображение",
        "достижение", "правительство", "исследование", "вдохновение", "программирование",
        "экономика", "демократия", "цивилизация", "ответственность", "независимость",
        "конкурентоспособность", "международный", "самосовершенствование", "окружающая среда", "искусственный интеллект"
    ]
}

# настройки записи
duration = 5
sample_rate = 44100

def record_and_recognize():
    print("[ говори у тебя 5 секунд ]")
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype="int16")
    sd.wait()
    wav.write("output.wav", sample_rate, recording)

    recognizer = sr.Recognizer()
    with sr.AudioFile("output.wav") as source:
        audio = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio, language="en-US")
        return text.lower()
    except:
        return None

def get_translation(word):
    result = GoogleTranslator(source="ru", target="en").translate(word)
    return result.lower()

print("Игра на чтобы показать что ты тупой")
print("20 слов, 3 ошибки и ты идешь плакать")
print("")

print("Выбери уровень сложности:")
print("1 - Легкий   | для молоденцев")
print("2 - Средний  | школьный уровень")
print("3 - Сложный  | для гениев но не для тебя(")

choice = input("Твой выбор (1/2/3): ")

if choice == "1":
    level = "easy"
    level_name = "Легкий"
elif choice == "2":
    level = "medium"
    level_name = "Средний"
elif choice == "3":
    level = "hard"
    level_name = "Сложный"
else:
    print("непонятно, ставлю легкий")
    level = "easy"
    level_name = "Легкий"

print("")
print("Уровень:", level_name)
input("Нажми Enter чтобы начать")

words = words_by_level[level].copy()
random.shuffle(words)

score = 0
mistakes = 0

for i in range(len(words)):
    if mistakes >= 3:
        break

    word = words[i]
    correct = get_translation(word)

    print("")
    print("Слово", i+1, "из", len(words))
    print("Счёт:", score, "  Ошибки:", mistakes, "из 3")
    print("RU:", word, "--> произнеси по английски")

    recognized = record_and_recognize()

    if recognized is None:
        print("Не понятно")
        print("Правильно:", correct)
        mistakes += 1
        continue

    print("Ты сказал:", recognized)
    print("Правильно:", correct)

    if recognized == correct or correct in recognized or recognized in correct:
        print("[ВЕРНО] +1")
        score += 1
    else:
        print("[НЕВЕРНО]")
        mistakes += 1

    time.sleep(0.8)

print("")
print("ИГРА ОКОНЧЕНА")
print("Результат:", score, "из", len(words))

if mistakes >= 3:
    print("3 ошибки ты вообще туопй?")
else:
    print("Ты прошёл давай все молодец")

if score == len(words):
    print("[***] Легенда но это очень легко броо")
elif score >= 15:
    print("[** ] Отлично ты чо с читами?")
elif score >= 10:
    print("[*  ] Хорошо но все ровно иди учись")
elif score >= 5:
    print("[.  ] Неплохо, но ты все ровно слаб")
else:
    print("[   ] Не сдавайся все ровно таким же тупым будешь")

again = input("ну чо потреним еще? (да/нет): ")
if again != "да":
    print("нууу понятно дурачок уже все облинился!!!!")
