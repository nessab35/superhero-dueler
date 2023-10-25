# dog.py
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        print("Dog initialized!")

    def bark(self):
        print(f"{self.name} Woof!")

    def sit(self):
        print(f"{self.name} sits")

    def rollover(self):
        print(f"{self.name} rolls over")
