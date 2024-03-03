# Запуск проекта локально

## Установка pytohn

```shell
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.12
sudo apt install python3-pip
```

## Установка окружения
```shell
cp .env.dist .env
pip install -r requirements.txt
```

## Запуск миграций
```
python manage.py migrate
```

## Запуск проекта локально
```
python manage.py runserver
```