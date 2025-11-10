from config import Exchanges
from connection import channel
import pika

routing_keys = ['user.signup', 'user.login', 'admin.login']

print("Enviando mensajes con producer topic.")

for key in routing_keys:
    channel.basic_publish(
        exchange=Exchanges.TOPIC_EXCHANGE,
        routing_key=key,
        body=key,
        properties=pika.BasicProperties(delivery_mode=pika.DeliveryMode.Persistent)
    )
