FROM python:3.5-alpine
WORKDIR /code
ADD requirements.txt /code
RUN pip install -r requirements.txt 
ADD consumer.py /code
