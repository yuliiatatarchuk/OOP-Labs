class MathTool:
    def add(self, a, b):
       return a + b
    def sub(self, a, b):
       return a - b
    def mul(self, a, b):
       return a * b

    def div(self, a, b):
        if b == 0:
            raise ValueError("Ділення на нуль неможливе")
        return a / b

class LibraryItem:
    def __init__(self, title, author,year):
        self.title = title
        self.author = author
        self.year = year
    def details(self):
        return f"{self.title}, {self.author}, {self.year}"

class NotificationService:
    def send(self, message):
        print(f"Відправка повідомлення: {message}")

class UserManager:
    def __init__(self, service):
        self.service = service

    def notify_user(self, user_name, message):
        full_message = f"Hello, {user_name}! {message}"
        self.service.send(full_message)

def check_even(number):
    return number % 2 == 0