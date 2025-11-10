from config import Queues
from connection import connection, channel

counter = 0


def callback_manual(ch, method, properties, body):
    print(f"Mensaje recibido de producer manual: {body.decode()}")
    ch.basic_ack(delivery_tag=method.delivery_tag)

def callback_automatic(ch, method, properties, body):
    global counter
    counter += 1
    if counter % 20 == 0:
        print(f"Numero de mensajes recibidos de producer automatico: {counter}")
    ch.basic_ack(delivery_tag=method.delivery_tag)

def make_fanout_callback(queue_name):
    counter_fanout = 0
    def callback(ch, method, properties, body):
        nonlocal counter_fanout
        counter_fanout += 1
        if counter_fanout % 20 == 0:
            print(f"Mensajes recibidos de {queue_name}: {counter_fanout}")
        ch.basic_ack(delivery_tag=method.delivery_tag)
    return callback


channel.exchange_declare(exchange='fanout', exchange_type='fanout', durable=True)

channel.queue_declare(queue=Queues.MANUAL_QUEUE, durable=True)
channel.queue_declare(queue=Queues.AUTOMATIC_QUEUE, durable=True)
channel.queue_declare(queue=Queues.FANOUT_QUEUE_1, durable=True)
channel.queue_declare(queue=Queues.FANOUT_QUEUE_2, durable=True)


channel.queue_bind(exchange='fanout', queue=Queues.FANOUT_QUEUE_1)
channel.queue_bind(exchange='fanout', queue=Queues.FANOUT_QUEUE_2)

channel.basic_consume(queue=Queues.MANUAL_QUEUE, on_message_callback=callback_manual)
channel.basic_consume(queue=Queues.AUTOMATIC_QUEUE, on_message_callback=callback_automatic)
channel.basic_consume(queue=Queues.FANOUT_QUEUE_1, on_message_callback=make_fanout_callback(Queues.FANOUT_QUEUE_1))
channel.basic_consume(queue=Queues.FANOUT_QUEUE_2, on_message_callback=make_fanout_callback(Queues.FANOUT_QUEUE_2))


try:
    print("Esperando mensajes.")
    channel.start_consuming()
except KeyboardInterrupt:
    connection.close()