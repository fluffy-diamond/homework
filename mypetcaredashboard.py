class Pet:
    def __init__(self, name, health):
        self.name = name
        self.__health = health   

    def info(self):
        print("The name is", self.name)
        print("The health level is",self.__health)

    def set_health(self, new_health):
        self.__health = new_health
        print("The health of you pet is now",self.__health)\

    def care(self):
        pass

class Dog(Pet):
    def care(self):  
        print(self.name,"needs to eat")

class Cat(Pet):
    def care(self):  
        print(self.name,"needs to eat")

class Rabbit(Pet):
    def care(self):  
        print(self.name,"needs to eat")


d = Dog("Peter", 50)
c = Cat("Mary", 50)
r = Rabbit("Ned", 50)

for pet in [d, c, r]:
    pet.info()
    pet.care()

print()

d.set_health(100)
c.set_health(20)
r.set_health(55)
