## Запуск backen-приложения локально

### Установка pytohn

```shell
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update && sudo apt install python3.12 python3-pip
```

### Установка окружения
```shell
cp .env.dist .env
pip install -r requirements.txt
```

### Поднятие контейнеров с сервисами
```bash
sudo dockerd
sudo docker compose -f docker-compose-local-services.yml up
```
Если нужно накатить из бэкапа, раскоментить в docker-compose-local-services.yml
```
      - PGDATA=/var/lib/postgresql/data/pgdata
    volumes:
      - type: bind
        source: ./data/pgdata
        target: /var/lib/postgresql/data/pgdata
        
Перенести бэкап в папку ./data/pgdata. После чего выполнить команду выше.
После того, как DB создана накатить получится только после удаления образа.
```

### Запуск миграций
```shell
python manage.py migrate
```

### Запуск сервера 
```shell
python manage.py runserver
```