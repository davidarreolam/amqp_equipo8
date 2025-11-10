from config import Queues
from connection import connection, channel
import pika
import random

MESSAGES_TO_SEND = 300

try:
    for i in range(MESSAGES_TO_SEND):
        msg = str(random.randint(1, 100))

        channel.basic_publish(
            exchange='',
            routing_key=Queues.AUTOMATIC_QUEUE,
            body=msg,
            properties=pika.BasicProperties(
                delivery_mode=pika.DeliveryMode.Persistent
            )
        )

        if i % 20 == 0:
            print(f'{i}/{MESSAGES_TO_SEND} mensajes enviados')

except KeyboardInterrupt:
    print('\n✗ Interrumpido')
finally:
    connection.close()