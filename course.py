from abc import ABC , abstractclassmethod 

class course (ABC) : 
    def __init__ (self, code, name, instructor) :
        self.code = code 
        self.name = name
        self.instructor = instructor
    @abstractclassmethod
    def disp(self) :
        pass 

class labc (course) : 
    def __init__ (self,code, name, instructor, location ) :
        super().__init__(code, name, instructor)
        self.location = location
    def disp(self) :
        print(f"Course Code: {self.code} and Course Name: {self.name}")        
        print(f"Course Instructore: {self.instructor}")
        print(f"Course Location: {self.location}")

class onlinec (course) : 
    def __init__ (self, code, name, instructor, platform) : 
        super().__init__(code, name, instructor)
        self.platform = platform
    def disp(self) : 
        print(f"Course Code: {self.code} and Course Name: {self.name}")        
        print(f"Course Instructore: {self.instructor}")
        print(f"Course Platform: {self.platform}")

l1 = labc("1001", "coding" , "jamal" , "b18-f1.09")
o1 = onlinec("2002" , "art" , "duha" , "zoom")   
print("first course details")
l1.disp()
print("second course details") 
o1.disp()    
