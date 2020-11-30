FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY backend-project/requirements/base.txt /code/
RUN pip install -r base.txt
COPY . /code/


