import os
from dotenv import load_dotenv

load_dotenv()

class AMQPConfig:
    URL = os.getenv('AMQP_URL')

class Queues:
    MANUAL_QUEUE = 'manual_queue'
    AUTOMATIC_QUEUE = 'automatic_queue'
    FANOUT_QUEUE_1 = 'fanout_queue_1'
    FANOUT_QUEUE_2 = 'fanout_queue_2'
    HEADER_QUEUE = 'header_queue'

class Exchanges:
    HEADER_EXCHANGE = 'header'
    FANOUT_EXCHANGE = 'fanout'
    TOPIC_EXCHANGE = 'topic'
