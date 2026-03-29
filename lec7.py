class x : 
    s = None 
    @staticmethod
    def get_instance():
        if x.s is None :
            x.s = x()
        return x.s
    def __init__ (self) : 
         self.data = []
    def add (self, v) : 
        self.data.append(v) 
    def getd (self) : 
        return self.data 

o1 = x.get_instance()
o2 = x.get_instance()
o1.add(10)
o2.add(20)
print(o1.getd())
print(o2.getd())             
