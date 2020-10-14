# Web framework bootstrap

На різних проектах використовують різні версії інтерпритатора, інструменти для створення віртуальних Python середовищ та управління залежностями. Для нових членів команди важливо вміти підлаштуватись під ті інструменти які вже використовуються в проекті.

Для командної роботи та збереження історії змін використовують системи контролю версій (наприклад, Git). Для збереження репозиторію часто використовують платформи типу GitHub, GitLab, Bitbucket та інші. 

В даній лабораторній роботі потрібно ініціалізувати проект інструментами згідно з варіантом, створити простий Flask-проект та запустити його використовуючи WSGI сервер. Також в репозиторії має бути файл `README.md` з інструкцією по розгортанню проекту після клонування (створення віртуального середовища і встановлення залежностей) з використанням відповідних інструментів. Створений код має бути збережений в системі контролю версій.

## Варіанти

Номер варіанту визначається номером студента в журналі. 

Можливі варіанти версії Python:
1. `3.8.*` 
2. `3.7.*` 
3. `3.6.*`

Можливі варіанти інструментів для створення віртуальних середовищ та управління залежностями:
1. [venv](https://docs.python.org/3/tutorial/venv.html) (вбудований в інтерпретатор) та requirements.txt
2. [virtualenv](https://virtualenv.pypa.io/en/stable/)
3. [poetry](https://python-poetry.org/)
4. [pipenv](https://pipenv.pypa.io/en/latest/)

Вимоги до конкретного варіанту можна визначити наступним чином (де `student_id` це номер варіанту студента):
```python
>>> from itertools import product
>>> list(product(
...     ('python 3.8.*', 'python 3.7.*', 'python 3.6.*'), 
...     ('venv + requirements.txt', 'virtualenv + requirements.txt', 'poetry', 'pipenv')
... ))[student_id - 1]
```

При попередньому узгодженню з викладачем можна 

## Хід роботи

1. Створити репозиторій у відповідній платформі (наприклад GitHub) та склонувати його, створити нову гілку
2. Інсталювати Python обраної версії за варіантом за допомогою [pyenv](https://github.com/pyenv/pyenv)    
3. Створити та активувати віртуальне Python середовище з інтерпретатором версії згідно з варіантом; якщо директорія віртуального середовища створена в директорії проекту, додати її в файл `.gitignore` (саме віртуальне середовище не має комітитись в репозиторій)
4. Добавити `Flask` в залежності проекту та інсталювати його (виконується по-різному залежно від варіанту)
5. Реалізувати адресу `api/v1/hello-world-{номер варіанту}`, що буде відповідати текстом `Hello World {номер варіанту}` з HTTP статус кодом відповіді `200`; Запустити та перевірити правильність виконання
6. Запустити проект використовуючи WSGI сервер (gunicorn, uWSGI чи інший на вибір)
    > На вибір бо, наприклад, gunicorn не підтримує Windows
7. Закомітити та запушити створені файли в репозиторій у попередньо створену гілку
8. Злити гілку з кодом лабораторної з гілкою `master` за допомогою Pull request (він жє ж Merge request) у відповідній платформі ([приклад виконання](https://docs.github.com/en/free-pro-team@latest/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request) для GitHub)
    > Трохи важко це перевірити, але хай спробують хто хоче
9. У файлі `README.md` описати інструкцію по розгортанню проекту

## Критерії оцінювання

1. Git
    * Перевірити наявність репозиторію на відповідній платформі (GitHub, GitLab чи іншій)
    * Перевірити наявність комітів
    > Командою `git log HEAD` або через візуальний інтерфейс
2. Python
    * Перевірити чи версія Python у активованому віртуальнму середовищі відповідає варіанту
    > Виконання команди `python --version` має видавати відповідну версію
    * Перевірити наявність віртуального середовища
    > Виконання команди `which python` (`where python` у Windows) має вказувати на інтерпритатор у віртуальному середовищі а не на системний, коли віртуальне середовище активоване
    * Перевірити що `Flask` вказаний в залежностях
    > Залежності можуть вказуватись у файлі `requirements.txt` або у іншому файлі залежно від інструменту управління залежностями
3. Реалізація адреси
    * Студент має запустити проект WSGI-сервером (не через`flask run`)
    * GET запит на `http://localhost:{порт}/api/v1/hello-world-{номер варіанту}` віддає текст "Hello World {номер варіанту}" та має HTTP статус код 200
    > Перевірити виконанням `curl -v -XGET http://localhost:5000/api/v1/hello-world-3` або у браузері
4. Студент має описати процес розгортання проекту з файлу `README.md`

## Виконання лабораторної роботи

### Створити репозиторій, склонувати його, створити нову гілку

Створити GitHub репозиторій і склонувати, створити нову гілку
```shell script
$ git clone ${REPO_ADDRESS}
$ git checkout -b lab-1
```

### Інсталювати Python обраної версії

```shell script
$ pyenv install 3.7.9
$ pyenv global 3.7.9
```

### Створити віртуальне середовище та додати його в `.gitignore`

#### venv + requirements.txt
```shell script
$ python -m venv ./env
$ echo "env/" >> .gitignore
$ source ./env/bin/activate
```

#### virtualenv + requirements.txt
```shell script
$ pip install virtualenv
$ virtualenv venv
$ echo "venv/" >> .gitignore
$ source ./venv/bin/activate
```

#### poetry
```shell script
$ curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
$ ~/.poetry/bin/poetry new poetry-lab-1
$ ~/.poetry/bin/poetry install
$ source $(~/.poetry/bin/poetry env info --path)/bin/activate
```

# pipenv
```shell script
$ pip install pipenv
$ pipenv install
$ pipenv shell
```

### Додати Flask в залежності

#### venv & virtualenv

```shell script
$ echo "Flask" >> requirements.txt
$ pip install -r requirements.txt
```

#### poetry

```shell script
$ ~/.poetry/bin/poetry add Flask
```

Flask додано в `poetry-lab-1/pyproject.toml`

#### pipenv

```shell script
$ pipenv install Flask
```

Flask додано в `Pipfile`.

### Реалізувати адресу `api/v1/hello-world-{номер варіанту}`

Можна реалізувати з використанням [flask blueprints](https://flask.palletsprojects.com/en/1.1.x/blueprints/)

Перевірити:
```shell script
$ FLASK_APP=lab1/app.py flask run
$ curl -v -XGET http://localhost:5000/api/v1/hello-world-3
```

### Запустити проект використовуючи WSGI сервер

#### venv & virtualenv
```shell script
$ echo "gunicorn" >> requirements.txt
$ pip install -r requirements.txt
```
#### poetry
```shell script
$ ~/.poetry/bin/poetry add gunicorn
```
#### pipenv
```shell script
$ pipenv install gunicorn
```
#### Запуск
```shell script
$ gunicorn -b 127.0.0.1:5000 --log-level DEBUG lab1.app:app
$ curl -v -XGET http://localhost:5000/api/v1/hello-world-3
```

### Закомітити та запушити 

```shell script
$ git add .
$ git commit -m "Lab 1"
$ git push origin master
```

### Інструкція

Створено інструкцію по розгортанню та запуску проекту в файлі [README.instruction.md](./README.instruction.md).  
