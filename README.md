# XBlockTestTask
Test task for the candidate

1.Створити папку для клонування:
```console
mkdir testdir
cd testdir
```
Створити та активувати віртуальне оточення:
```console
virtualenv venv
venv\Scripts\activate.bat (для Windows)
source tutorial-env/bin/activate (для Linux та Mac OS)
```
Клонувати репозиторій:
```console
git clone https://github.com/Danil-Tolmachov/XBlockTestTask
```
Клонувати SDK:
```console
git clone https://github.com/openedx/xblock-sdk.git
cd xblock-sdk
pip install -r requirements/base.txt
```
Зробити міграції
```console
python manage.py migrate
cd ..
```
Встановити myxblock
```console
pip install -e myxblock
```
Запустити локальний сервер
```console
cd xblock-sdk
python manage.py runserver
```
Налаштувати заголовок та контент можна у файлі myblox/config.py
