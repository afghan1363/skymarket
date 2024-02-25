FROM python:3

WORKDIR /skymarket/

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY ./skymarket/ .