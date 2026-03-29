import threading
import time 

def task1 () :
    for i in range (5) :
       print(f"task1 - count {i}")
       time.sleep(2)

def task2 () :
    for i in range (5) :
       print(f"task2 - count {i}")
       time.sleep(2)


t1 = threading.Thread(target=task1)   
t2 = threading.Thread(target=task2)  
t1.start
t2.start