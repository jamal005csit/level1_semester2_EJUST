def calc (a , s) : 
    try :
        r = a / s
        print("resul:" , r)
    except ZeroDivisionError :
        print("Error: cannot divide by zero")
    except ValueError : 
        print("Error: enter valid number")
    except OverflowError : 
        print("Error: memory couldnot handle the result")
    except Exception as e : 
        print("ther is an Error:" , e)   


n = int(input("enter numerator"))
d = int(input("enter dumerator"))
calc(n,d)

print("first calc")
calc(5,5)
print("second calc")
calc(8,1)
print("third calc")
calc(1,0)                       
