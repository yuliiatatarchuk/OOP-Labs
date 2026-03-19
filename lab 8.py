import paho.mqtt.client as mqtt
import time
import requests
import asyncio
import websockets

REST_URL = "https://jsonplaceholder.typicode.com/posts/1"
WS_URL = "wss://ws.postman-echo.com/raw"
BROKER_ADDRESS = "broker.hivemq.com"
BROKER_PORT = 1883
TOPIC = "home/temperature"
MESSAGE = "15.3°C"


class MQTTClient():
    def __init__(self, broker_address, port):
        self.broker_address = broker_address
        self.port = port
        self.client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

    def on_connect(self):
        self.client.connect(self.broker_address, self.port)
        self.client.loop_start()
        print("Connected to MQTT broker")

    def on_publish(self, topic, message):
        self.client.publish(topic, message)
        print(f"Published to {topic}: {message}")

    def on_disconnect(self):
        self.client.loop_stop()
        self.client.disconnect()
        print("Disconnected from MQTT broker")


def get_data_from_rest():
    response = requests.get(REST_URL)
    data = response.json()
    message = data["title"]
    print("Data from REST:", message)
    return message


async def send_via_websocket(message):
    async with websockets.connect(WS_URL) as websocket:
        await websocket.send(message)
        print("Sent via WebSocket:", message)


async def main():
    data = get_data_from_rest()

    await send_via_websocket(data)
    mqtt_client = MQTTClient(BROKER_ADDRESS, BROKER_PORT)
    mqtt_client.on_connect()
    mqtt_client.on_publish(TOPIC, data)
    mqtt_client.on_disconnect()


asyncio.run(main())






