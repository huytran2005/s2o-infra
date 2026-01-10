import pika
import os
import time

# ===== ENV =====
RABBIT_HOST = os.getenv("RABBIT_HOST", "localhost")
RABBIT_PORT = int(os.getenv("RABBIT_PORT", "5672"))
RABBIT_USER = os.getenv("RABBIT_USER", "guest")
RABBIT_PASSWORD = os.getenv("RABBIT_PASSWORD", "guest")
QUEUE_NAME = os.getenv("QUEUE_NAME", "order_events")

print("=== WORKER STARTING ===")
print("RABBIT_HOST =", RABBIT_HOST)
print("RABBIT_PORT =", RABBIT_PORT)
print("RABBIT_USER =", RABBIT_USER)
print("QUEUE_NAME =", QUEUE_NAME)

# ===== MAIN LOOP =====
while True:
    try:
        # credentials
        credentials = pika.PlainCredentials(
            RABBIT_USER,
            RABBIT_PASSWORD
        )

        # connection params
        parameters = pika.ConnectionParameters(
            host=RABBIT_HOST,
            port=RABBIT_PORT,
            credentials=credentials,
            heartbeat=60,
            blocked_connection_timeout=300
        )

        # connect
        connection = pika.BlockingConnection(parameters)
        channel = connection.channel()

        # ensure queue exists
        channel.queue_declare(queue=QUEUE_NAME, durable=True)

        def callback(ch, method, properties, body):
            print("[x] Received:", body.decode())
            ch.basic_ack(delivery_tag=method.delivery_tag)

        channel.basic_consume(
            queue=QUEUE_NAME,
            on_message_callback=callback,
            auto_ack=False
        )

        print("[*] Waiting for messages...")
        channel.start_consuming()

    except Exception as e:
        print("ERROR:", repr(e))
        time.sleep(5)
