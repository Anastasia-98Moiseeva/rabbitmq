#!/usr/bin/env python
import pika
import time

def callback(ch, method, properties, body):
    print('Consumer received number ', body, flush = True)

time.sleep(10)

connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq', 5672, '/', pika.PlainCredentials('guest', 'guest')))
channel = connection.channel()

channel.queue_declare(queue='random_generator')

channel.basic_consume(callback, queue='random_generator', no_ack=True)

try:
    channel.start_consuming()
except KeyboardInterrupt:
    channel.stop_consuming()
