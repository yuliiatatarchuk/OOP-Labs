import requests

url = "https://jsonplaceholder.typicode.com"
data = {"title":"Мій новий пост", "body":"Мій пост це текст", "userId":1}
class RestClient():
    def __init__(self,base_url):
        self.base_url = base_url.rstrip('/')
    def get_data(self,endpoint):
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print(data[:2])
        else:
            print("Помилка:", response.status_code)

    def post_data(self, endpoint,data):
        url = f"{self.base_url}/{endpoint}"
        response = requests.post(url, json=data)
        if response.status_code == 201:
            print("Створено пост:", response.json())
        else:
            print("Помилка:", response.status_code)

client = RestClient(url)
client.get_data("posts")
client.post_data("posts", data)