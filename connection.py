import pika

from config import AMQPConfig

print('Conectando a servidor.')
connection = pika.BlockingConnection(pika.URLParameters(AMQPConfig.URL))
channel = connection.channel()