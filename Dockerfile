FROM python:3.7

WORKDIR /app

COPY requirements.txt /app

COPY . .

RUN pip install -r requirements.txt

