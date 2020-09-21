# Інструкція по розгортанню проекту

1. Встановити Python 3.7.9
2. СТворити вірутальне середовище командою `python -m venv ./env` і активувати `source ./env/bin/activate`
3. Встановити залежності командою `pip install -r requirements.txt`
4. Запустити проект командою `gunicorn -b 127.0.0.1:5000 app:app`