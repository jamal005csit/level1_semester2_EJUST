class realimage :
    def __init__ (self, name ) : 
        self.name = name 
        self.loading()
    def loading(self) : 
        print(f"loading {self.name}")
    def disp(self) : 
        print(f"displaying {self.name}")

class proxyimage : 
    def __init__ (self, name) : 
        self.name = name
        self.x = None 
    def disp(self) : 
        if self.x is None :
            print(f"creating {self.name}")
            self.x = realimage(self.name)
        self.x.disp()   

i1 = proxyimage("file1")
i1.disp()
i1.disp()

i2 = proxyimage("file2")
i2.disp()

