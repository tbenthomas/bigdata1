FROM python:3.7

RUN mkdir /app

WORKDIR /app

COPY requirements.txt /app

COPY . .

RUN pip install -r requirements.txt

ENV APP_KEY=_


