FROM python:3.10

WORKDIR /skymarket

COPY ./requirements.txt .

RUN pip install -r requirements.txt

ENV PYTHONUNBUFFERED=1

COPY ./skymarket/. .

COPY .env .