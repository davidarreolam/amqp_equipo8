from config import Exchanges
from connection import channel
import pika


headers_list = [
    {'format': 'pdf', 'type': 'report'},
    {'format': 'csv', 'type': 'report'},
]

print("Enviando mensajes con producer fanout.")

for headers in headers_list:
    msg = f"{headers['format']}"
    channel.basic_publish(
        exchange=Exchanges.HEADER_EXCHANGE,
        routing_key='',
        body=msg,
        properties=pika.BasicProperties(
            headers=headers,
            delivery_mode=pika.DeliveryMode.Persistent
        )
    )
