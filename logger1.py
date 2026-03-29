class logger : 
    s = None 
    @staticmethod
    def get_instance():
        if logger.s is None :
            logger.s = logger()
        return logger.s 
    def __init__ (self) : 
        self.logh = [] 
    def add (self, m) : 
        self.logh.append(m)
    def getin(self) : 
        print(self.logh)


l1 = logger.get_instance()
l2 = logger.get_instance()
l1.add("lolo")
l2.add("hoho")
l1.getin()
l2.getin()                  