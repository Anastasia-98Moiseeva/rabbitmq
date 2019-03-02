FROM python:3.5-alpine
WORKDIR /code
ADD requirements.txt /code
RUN pip install -r /code/requirements.txt
ADD producer.py /code
