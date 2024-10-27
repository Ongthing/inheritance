#inheritance
class Animal:
    alive = True
    def eat(self):
        print("this animal is eating")
    def slumber(self):
        print("this animal is sleeping")
class Rabbit(Animal):
    def run(self):
        print("This rabbit is running")
class Fish(Animal):
    def swim(self):
        print("this fish is swimming")
class Hawk(Animal):
    def fly(self):
        print("this hawk is flying")
rabbit = Rabbit()
fish = Fish()
hawk = Hawk()
#print(rabbit.alive)
#fish.eat()
#hawk.sleep()
rabbit.run()
fish.swim()
hawk.fly()

#multi_level inheritance = when a derived (child) class inherits another derived (child) class

class organism:
    alive = True
class Animal(organism):
    def eat(self):
        print("this animal is eating")
class Dog(Animal):
    def bark(self):
        print("thsi dog is barking")

dog = Dog()
print(dog.alive) #inherited from the organism class
dog.eat() #inherited from the animal class
dog.bark() #defined in dog class

#mulitple inheritance = when a child is derived from more then one parent class

class prey:
    def flee(self):
        print("this animal flees")
class predator:
    def hunt(self):
        print("this animal is hunting")

class Rabbit(prey):
    pass
class Hawk(predator):
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee()
hawk.hunt()

#fish.flee()
#fish.hunt()

#CHANGE CLASS

class Animal:
    def eat(self):
        print("this animal is eating")
class Rabbit(Animal):

    def eat(self):
        print("this rabbit is eating a carrot")
rabbit = Rabbit()
rabbit.eat()