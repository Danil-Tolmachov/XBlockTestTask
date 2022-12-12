# XBlockTestTask
Test task for the candidate

1. Створити папку для клонування:
```console
mkdir testdir
cd testdir
```
2. Створити та активувати віртуальне оточення:
```console
virtualenv venv
venv\Scripts\activate.bat (для Windows)
source tutorial-env/bin/activate (для Linux та Mac OS)
```
3. Клонувати репозиторій:
```console
git clone https://github.com/Danil-Tolmachov/XBlockTestTask
```
4. Клонувати SDK:
```console
git clone https://github.com/openedx/xblock-sdk.git
cd xblock-sdk
pip install -r requirements/base.txt
```
5. Зробити міграції
```console
python manage.py migrate
cd ..
```
6. Встановити myxblock
```console
pip install -e myxblock
```
7. Запустити локальний сервер
```console
cd xblock-sdk
python manage.py runserver
```
Налаштувати заголовок та контент можна у файлі myblox/config.py

Якщо при першому включеннi виникає помилка - спробувати перезавантажити сторiнку.
