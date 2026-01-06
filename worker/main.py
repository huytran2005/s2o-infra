import pika
import json
import os
import time

RABBIT_HOST = os.getenv("RABBIT_HOST", "localhost")
QUEUE_NAME = os.getenv("QUEUE_NAME", "order_events")

print("=== WORKER STARTING ===")
print("RABBIT_HOST =", RABBIT_HOST)
print("QUEUE_NAME =", QUEUE_NAME)

while True:
    try:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=RABBIT_HOST)
        )
        channel = connection.channel()

        channel.queue_declare(queue=QUEUE_NAME, durable=True)

        def callback(ch, method, properties, body):
            print(" [x] Received:", body.decode())
            ch.basic_ack(delivery_tag=method.delivery_tag)

        channel.basic_consume(
            queue=QUEUE_NAME,
            on_message_callback=callback,
            auto_ack=False
        )

        print(" [*] Waiting for messages...")
        channel.start_consuming()

    except Exception as e:
        print("ERROR:", e)
        time.sleep(5)
