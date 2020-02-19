FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /testeambar
WORKDIR /testeambar

RUN apt-get update && apt-get upgrade -y && apt-get install -y \
libsqlite3-dev

RUN pip install -U pip setuptools

COPY requirements.txt /testeambar/

RUN pip install -r /testeambar/requirements.txt

ADD . /testeambar/

RUN export FLASK_APP=app.py && export FLASK_ENV=development

RUN flask db upgrade

# Flask service
EXPOSE 5000
