from connection import connection, channel
import pika
import random

MESSAGES_TO_SEND = 300

try:
    for i in range(MESSAGES_TO_SEND):
        msg = str(random.randint(1, 100))
        channel.basic_publish(
            exchange='fanout',
            routing_key='',
            body=msg,
            properties=pika.BasicProperties(
                delivery_mode=pika.DeliveryMode.Persistent
            )
        )
except KeyboardInterrupt:
    print('\n✗ Interrumpido')
finally:
    connection.close()
