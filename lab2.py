class Vehicle:
    def __init__(self,speed):
        self.speed=speed
    def drive(self):
        print(f"Машина їде зі швидкістю {self.speed}")
class Car(Vehicle):
        def __init__(self,speed,brand):
            super().__init__(speed)
            self.brand=brand
        def drive(self):
            print(f"{self.brand} їде зі швидкістю {self.speed}")
Car=Car(200,"Toyota")
Car.drive()


class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def introduce(self):
        print(f"Привіт. Мене звуть {self.name}, мені {self.age} років")
class Student(Person):
    def __init__(self,name,age, university):
        super().__init__(name,age)
        self.university=university
    def introduce(self):
        print(f"мене звуть {self.name} мені {self.age} років, я навчаюсь в {self.university}")
st1=Student("Yuliia",18, "LPNU")
st1.introduce()


class Teacher:
    def teach(self):
        return "Teaching at school"
class Researcher(Teacher):
    def research(self):
        return "Do a research work"
class Professor(Researcher):
    def teach(self):
        super().teach()
        return "Teaching in university"
pr1=Professor()
print(pr1.teach())
class ElectricDevice:
    def turn_on(self):
        return "is On"
class BatteryPowered(ElectricDevice):
    def __init__(self, battery_lvl):
        self.battery_lvl=battery_lvl
class Smartphone(BatteryPowered):
    def use_app(self):
        return "App is not using"
dev=Smartphone(5)
print(dev.use_app())


class Shape:
    def area(self):
        pass
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*(self.radius)
class Rectangle(Circle):
    def __init__(self, width,height):
        self.width=width
        self.height=height
    def area(self):
        return (self.width)*(self.height)
sh=Circle(4)
sh1=Rectangle(5,6)
print(sh.area())
print(sh1.area())


class A:
    def say(self):
        return "A"
class B(A):
    def say(self):
        return "B" + super().say()
class C(A):
    def say(self):
     return "C" + super().say()
class D(B, C):
    def say(self):
        return "D" + super().say()
E = D()
print(E.say())


class Engine:
    def start(self):
        pass
class CarInheritance(Engine):
    pass
class CarComposition:
    def __init__(self):
            self.engine = Engine()
    def start_engine(self):
            self.engine.start()
            print("Наслідування:")
car1 = CarInheritance()
car1.start()

print("Композиція:")
car2 = CarComposition()
car2.start_engine()