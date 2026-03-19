import websockets
import asyncio

url = "wss://ws.postman-echo.com/raw"
class WebSocketClient:
    def __init__(self):
      self.connection = None
    async def connect(self, url):
        try:
         self.connection = await websockets.connect(url, open_timeout=10)
         print(f"Підключено")
        except Exception as e:
         print(f"Помилка підключення: {e}")
         self.connection = None

    async def send(self, message):
      await self.connection.send(message)
      print(message)

    async def receive(self):
       message = await self.connection.recv()
       return message

    async def close_connection(self):
     if self.connection:
        await self.connection.close()
        print("З'єднання закрите.")

client = WebSocketClient()

async def main():
 client = WebSocketClient()
 await client.connect(url)

 if client.connection:
  await client.send("I love cookies")
  response = await client.receive()
  print(f"Отримано від сервера: {response}")
  await client.close_connection()

asyncio.run(main())