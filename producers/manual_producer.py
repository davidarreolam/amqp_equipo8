from config import Queues
from connection import connection, channel
import pika

try:
    while True:
        msg = input('Escribe un mensaje para mandar a la cola: ')
        channel.basic_publish(
            exchange='',
            routing_key=Queues.MANUAL_QUEUE,
            body=msg,
            properties=pika.BasicProperties(
                delivery_mode=pika.DeliveryMode.Persistent
            )
        )
        print('Mensaje enviado')
except KeyboardInterrupt:
    connection.HHclose()