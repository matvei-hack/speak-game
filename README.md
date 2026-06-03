🔊 1. Установка библиотек для распознавания речи

Выполните команду:

sudo dnf install -y portaudio portaudio-devel alsa-lib-devel

⚠️ После ввода команды система попросит ввести ваш sudo-пароль.

📂 2. Перейдите в папку проекта

Замените имя_проекта на название вашей папки:

cd ~/Desktop/имя_проекта

📁 Эта команда перенесёт вас в директорию проекта.

🗑️ 3. Удалите старое виртуальное окружение (если оно есть)
rm -rf venv

✨ Это поможет избежать возможных ошибок со старыми зависимостями.

🐍 4. Создайте новое виртуальное окружение Python 3.13
python3.13 -m venv venv
✅ 5. Активируйте виртуальное окружение
source venv/bin/activate

После активации вы увидите (venv) в начале строки терминала.

📦 6. Установите все необходимые библиотеки
pip install sounddevice scipy numpy SpeechRecognition deep-translator

Будут установлены следующие библиотеки:

🎤 sounddevice
📊 scipy
🔢 numpy
🗣️ SpeechRecognition
🌍 deep-translator
🚀 7. Запуск игры
python main.py

🎉 Готово! Игра должна запуститься.

⚡ Быстрая установка (все команды подряд)
sudo dnf install -y portaudio portaudio-devel alsa-lib-devel

cd ~/Desktop/имя_проекта

rm -rf venv

python3.13 -m venv venv

source venv/bin/activate

pip install sounddevice scipy numpy SpeechRecognition deep-translator

python main.py

🎮 Приятной игры и удачи в изучении английского языка! 🇬🇧✨
