class person : 
    """Auto-generated docstring for:
class person : 
    def __init__ (self, name) :
    """Auto-generated docstring for:
def __init__ (self, name) :
        self.__name = name"""
        self.__name = name
    def dispn(self) : 
    """Auto-generated docstring for:
def dispn(self) : 
        return self.__name"""
        return self.__name"""
    def __init__ (self, name) :
    """Auto-generated docstring for:
def __init__ (self, name) :
        self.__name = name"""
        self.__name = name
    def dispn(self) : 
    """Auto-generated docstring for:
def dispn(self) : 
        return self.__name"""
        return self.__name   
    
class student (person) :
    """Auto-generated docstring for:
class student (person) :
    def __init__ (self, name, id, ) : 
    """Auto-generated docstring for:
def __init__ (self, name, id, ) : 
        super().__init__(name)
        self.__id = id 
        self.cousre = []"""
        super().__init__(name)
        self.__id = id 
        self.cousre = [] 
    def enroll (self, c) :
    """Auto-generated docstring for:
def enroll (self, c) :
        self.cousre.append(c)"""
        self.cousre.append(c) 
    def disp (self) : 
    """Auto-generated docstring for:
def disp (self) : 
        print(f"student name: {self.dispn()}")    
        print(f"student id: {self.__id}")
        print(f"attended courses: {self.c}")"""
        print(f"student name: {self.dispn()}")    
        print(f"student id: {self.__id}")
        print(f"attended courses: {self.c}")"""
    def __init__ (self, name, id, ) : 
    """Auto-generated docstring for:
def __init__ (self, name, id, ) : 
        super().__init__(name)
        self.__id = id 
        self.cousre = []"""
        super().__init__(name)
        self.__id = id 
        self.cousre = [] 
    def enroll (self, c) :
    """Auto-generated docstring for:
def enroll (self, c) :
        self.cousre.append(c)"""
        self.cousre.append(c) 
    def disp (self) : 
    """Auto-generated docstring for:
def disp (self) : 
        print(f"student name: {self.dispn()}")    
        print(f"student id: {self.__id}")
        print(f"attended courses: {self.c}")"""
        print(f"student name: {self.dispn()}")    
        print(f"student id: {self.__id}")
        print(f"attended courses: {self.c}")

class courses :
    """Auto-generated docstring for:
class courses :
    def __init__ (self, cc, cn) :
    """Auto-generated docstring for:
def __init__ (self, cc, cn) :
        self.cc = cc
        self.cn = cn"""
        self.cc = cc
        self.cn = cn"""
    def __init__ (self, cc, cn) :
    """Auto-generated docstring for:
def __init__ (self, cc, cn) :
        self.cc = cc
        self.cn = cn"""
        self.cc = cc
        self.cn = cn 

s1 = student("jamal" , "181") 
s2 = student("jana" , "145")      
c1 = courses("8008" , "csc")
c2 = courses("9009" , "lra") 

s1.enroll(c1.cn)
s1.enroll(c2.cn)
s2.enroll(c2.cn)

s1.disp()
print("\n")
s2.disp()
