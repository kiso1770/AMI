FROM python:3.12 AS builder
WORKDIR /app
COPY . .
RUN /bin/bash -c 'cp .env.exemple .env'
RUN python -m venv venv &&  pip install --no-cache-dir -r requirements.txt

EXPOSE 8000