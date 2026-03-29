class animal : 
    def __init__ (self, name) : 
        self.name = name
        self.age = 0
    def eat (self) : 
        print(f"{self.name} is eating")
    def sleep(self):        
        print(f"{self.name} is sleeping")


class dog (animal) : 
    def __init__ (self, name, breed) :
        super().__init__(name)
        self.breed = breed
    def bark (self) : 
        print(f"{self.name} is barking")


d = dog("roxy" , "pitbull")
print(f"Name: {d.name}")
print(f"Breed: {d.breed}")
d.eat()
d.bark()
d.sleep()            
print(f"Age: {d.age}")