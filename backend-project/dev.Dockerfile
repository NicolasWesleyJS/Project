FROM python:3

ARG DJANGO_ENV
ENV DJANGO_ENV $DJANGO_ENV
ENV PYTHONUNBUFFERED=1

WORKDIR /api/

COPY requirements/base.txt /api/

RUN pip install -r base.txt

COPY . /api/

ENV DJANGO_SETTINGS_MODULE backend.settings.base