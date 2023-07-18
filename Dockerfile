FROM python:3.11

ENV PYTHONUNBUFFERED=1

WORKDIR /var/django-app/

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY M_13_DRF/mysite .


