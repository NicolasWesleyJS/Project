FROM python:3

ENV PYTHONUNBUFFERED=1

WORKDIR /api/

COPY requirements/base.txt /api/

RUN pip install -r base.txt

COPY . /api/
