FROM python:3

ARG DJANGO_ENV
ENV DJANGO_ENV $DJANGO_ENV
ENV PYTHONUNBUFFERED=1

WORKDIR /api/

COPY requirements/base.txt /api/

RUN pip install -r base.txt

COPY . /api/

ENV DJANGO_SETTINGS_MODULE backend.settings.base

RUN buildDeps='g++' && \
    apt-get update && apt-get install -y $buildDeps --no-install-recommends && \
    apt-get install -y --no-install-recommends libgraphviz-dev wait-for-it postgresql postgresql-contrib && \
    pip install --no-cache-dir -U pip && \
    apt-get purge -y --auto-remove $buildDeps