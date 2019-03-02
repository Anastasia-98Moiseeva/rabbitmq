#!/usr/bin/env python
import pika
import random
import time

def generate(channel, key):
    number = random.randint(-500, 500)
    #print('Producer sent number', number)
    channel.basic_publish(exchange='', routing_key=key, body=str(number))

time.sleep(10)
connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq', 5672, '/', pika.PlainCredentials('guest', 'guest')))
channel = connection.channel()

channel.queue_declare(queue='random_generator')

num = 10
for i in range(num):
    t = random.randint(0, 5)
    time.sleep(t)
    generate(channel, 'random_generator')

connection.close()
