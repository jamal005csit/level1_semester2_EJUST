try : 
    n1 = int(input("enter first number"))
    n2 = int(input("enter the second number"))

    r = n1 / n2 
    print(f"result: {r}")

except ValueError :
    print("Error: enter valid number")
except ZeroDivisionError : 
    print("cannot divide over zero")       

