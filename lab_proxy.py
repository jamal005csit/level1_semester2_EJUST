class realfile : 
    def __init__ (self,name) : 
        self.name = name
        self.c = "this is content"
        self.is_open = False 
    def open(self):
        if self.is_open is False :
            self.is_open = True 
            print(f"opening {self.name}")
    def close(self): 
        if self.is_open is True :
            self.is_open = False 
            print(f"{self.name} is closed")
        else : 
            print(f"{self.name} is already closed")    
       
    def read(self):     
        if self.is_open is True : 
            print (f"reading from {self.name}")
        else :
            print(f"cannot read as {self.name} is not opened yet")

class fileproxy :
    def __init__ (self, name , role ) : 
        self.name = name 
        self.role = role 
        self.r = None 
        data = [] 
    def open (self) : 
        if self.role != "admin" :
            fileproxy.data.append((self.role , "open" , "denied"))
            print(f"{self.role} can not open this file")
        else : 
            if not self.r : 
                self.r = realfile(self.name)
            self.r.open()
            fileproxy.data.append((self.role, "open" , "allowed"))    
