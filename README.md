# speak-game
my first eanglish game


# speak-game
my first eanglish game
это мой первый проект и вот как его запускать и какие библеотеки надо делал на федора линукс поэтому команды для этого диструбутива
все делать в консоли!!


sudo dnf install -y portaudio portaudio-devel alsa-lib-devel устоновить библеотеку для речи попросят вести ваш судо пароль
cd ~/Desktop/имя проекта как вы назвали это перекидывает чтобы вы могли работать в папке вашего проекта
rm -rf venv удалить вэнв если увас был чтобы без ошибок
python3.13 -m venv venv создаете новый вэнв 3.13
source venv/bin/activate активируйте вэнв
pip install sounddevice scipy numpy SpeechRecognition deep-translator устоновим все библеотеки
python main.py запуст кода
