FROM python:3

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt

ENV LANG ja_JP.UTF-8
ENV PYTHONIOENCODIND utf_8
