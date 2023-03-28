FROM python:3.10-alpine

MAINTAINER [ VALIKO666 ]

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV FLASK_APP server/__init__.py

WORKDIR /backend

COPY . /backend

RUN pip install --upgrade pip && pip install -r requirements.txt

#EXPOSE 5000