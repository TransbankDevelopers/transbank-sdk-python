FROM python:3.12.0a5-slim
RUN apt-get update && apt-get install -y python3-pip
RUN pip install pipenv
RUN mkdir -p /sdk
WORKDIR /sdk
COPY . /sdk
