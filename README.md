# Тестовое задание от компании "Ришат"

Test case for Rishat Company

## Требования

`python == 3.11`

## Клонирование репозитория

```bash
git clone https://github.com/Vek123/rishat-test.git
```

## Инструкция по запуску приложения (Debian Based)

### Подготовка к запуску

* Склонируйте репозиторий

```bash
git clone https://github.com/Vek123/rishat-test.git
```

* Установите необходимые пакеты системы

```bash
cd rishat-test
sudo apt-get update
sudo apt install python3.11
sudo apt-get -y install python3-venv
```

* Создайте виртуальное окружение и активируйте его

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Developer Mode

* Установите необходимые зависимости

```bash
pip3 install -r requirements/dev.txt
```

* Создайте файл .env с помощью шаблона template.env

```bash
cp template.env .env
# Заполнить файл .env
```

* Примените миграции

```bash
cd store
python3 manage.py migrate
```

* Запустите приложение

```bash
python3 manage.py runserver
```

### Production Mode

* Установите необходимые зависимости

```bash
pip3 install -r requirements/prod.txt
```

* Создайте файл .env с помощью шаблона template.env

```bash
cp template.env .env
# Заполнить файл .env
```

* Примените миграции

```bash
cd store
python3 manage.py migrate
```

* Запустите приложение

```bash
python3 manage.py runserver
```

### Запуск тестов

* Установите необходимые зависимости

```bash
pip3 install -r requirements/test.txt
```

* Создайте файл .env с помощью шаблона template.env

```bash
cp template.env .env
# Заполнить файл .env
```

* Запустите синтаксические тесты

```bash
flake8 --verbose
black --verbose .
```

* Запустите тесты приложения

```bash
cd store
python3 manage.py test
```
