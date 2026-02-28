#1.1
class CallReport:
    def report_call(self):
        print("Звіт сформовано")
class Data:
    def save_data(self):
        print("Дані збережено")
report = CallReport()
report.report_call()
db = Data()
db.save_data()

#1.2
class Subscriber:
    user="Іван Іванович"
    print(user)

class Message:
    print("SMS sent")

class Balance:
    print ("Your balance")

#2.1
class Tariff:
    def price(self, minutes):
        return 0

class BasicTariff(Tariff):
    def price(self, minutes):
        return minutes * 1

class NewTariff(Tariff):
    def price(self, minutes):
        return minutes * 2

#2.2
class BaseTariff:
    def calc_cost(self, usage):
        pass
class VoiceTariff(BaseTariff):
    def calc_cost(self, usage):
        return usage*2
class DataTariff(BaseTariff):
    def calc_cost(self, usage):
        return usage*1.5
class RoamingTariff(BaseTariff):
    def calc_cost(self, usage):
        return usage*5

#3.1
class NetworkConnection:
    def connect(self):
        print("Підключення до мережі")

class WiFiConnection(NetworkConnection):
    def connect(self):
        print("WiFi підключено")

class LTEConnection(NetworkConnection):
    def connect(self):
        print("LTE підключено")
#3.2
class SatelliteConnection(NetworkConnection):
    def connect(self):
        print ("Щоб підключити супутникове з'єднання укладіть договір")

#4.1
class Call:
    def make_call(self):
        print("Call")
class SMS:
    def send_sms(self):
        print("SmS")
class Network:
    def connect_to_network(self):
        print ("Connected to network")

class Nokia(Call,SMS):
    def make_call(self):
        print("Call")


    def send_sms(self):
        print("SmS")
class ModernPhone(Call, SMS, Network):
    def make_call(self):
        print("Call")


    def send_sms(self):
        print("SmS")


    def connect_to_network(self):
        print ("Connected to network")
#4.2

class DataTransfer:
    def send_data(self, data):
        pass
class IoTDevice(DataTransfer):
    def send_data(self, data):
        print(f"Дані з датчика: {data}")
#5.1
class Logger:
    def log(self, message):
        pass
class FileLogger(Logger):
    def log(self, message):
        print(f"Запис у файл: {message}")
class ServerLogger(Logger):
    def log(self, message):
        print(f"Відправка даних: {message}")

class ConsoleLogger(Logger):
    def log(self, message):
        print(f"Вивід у консоль: {message}")
class NetworkMonitor:
    def __init__(self, logger: Logger):
        self.logger = logger

    def check(self):
        self.logger.log("Мережа працює")
monitor_file = NetworkMonitor(FileLogger())
monitor_file.check()
monitor_server = NetworkMonitor(ServerLogger())
monitor_server.check()