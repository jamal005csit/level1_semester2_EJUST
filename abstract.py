from abc import ABC , abstractmethod

class shape(ABC) : 

    @abstractmethod
    def area (self) :
        pass 

    @abstractmethod
    def perimeter (self) : 
        pass 

class rectangle (shape) :
    def __init__ (self, l , w) : 
        self.l = l 
        self.w = w 
    def area (self) : 
        self.x = self.l * self.w 
        print (f"Area: {self.x}")   
    def perimeter(self):
        self.x = 2 *  (self.l + self.w) 
        print (f"Perimeter: {self.x}") 

r1 = rectangle (5 , 3)
r1.area()
r1.perimeter()
                 