class book :
    def __init__ (self, title = '' , author = '') :
        self.title = title 
        self.author = author
    def set (self, title , author) :
        self.title = title 
        self.author = author 
    def disp (self) :
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
class fiction (book) : 
    def __init__ (self, title , author, grade=0) :   
        super().__init__(title , author)  
        self.grade = grade
    def set (self, title , author, grade) :
        super().set(title , author)
        self.grade = grade
    def disp (self) :
        super().disp()
        print(f"Grade Level: {self.grade}")

class nonfiction (book) : 
    def __init__ (self, title , author, pages=0) :   
        super().__init__(title , author)  
        self.pages = pages
    def set (self, title , author, pages) :
        super().set(title , author)
        self.pages = pages
    def disp (self) :
        super().disp()
        print(f"Number of Pages: {self.pages}")


f = fiction("wizard" , "tesla" , 5)
n = nonfiction("seduction" , "karnegy" , 369)  
f.disp()
n.disp()      
