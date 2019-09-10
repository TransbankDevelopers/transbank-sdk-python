FROM python:3.7.4-stretch
RUN apt-get update && apt-get install -y python3-pip
RUN pip install pipenv
RUN mkdir -p /sdk
WORKDIR /sdk
COPY . /sdk
