FROM python:3.8.6
ENV PYTHONUNBUFFERED 1
ENV REDIS_HOST "jokes-redis"
RUN mkdir /code
WORKDIR /code
RUN apt-get update && apt-get install -y
COPY requirements.txt /code/
RUN pip install -r requirements.txt
RUN pip install --upgrade pip
ADD . /code/
