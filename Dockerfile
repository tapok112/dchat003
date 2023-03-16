FROM python:3.10
RUN apt-get update -qq && apt-get install -y
RUN apt-get install ffmpeg -y
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt --no-cache-dir

