class Point:
    def draw(self):
        print("draw")
    def move(self):
        print("move")


point1 = Point()
# point1.move()

class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi! I am {self.name}")

person = Person("hrithik")
person.talk()