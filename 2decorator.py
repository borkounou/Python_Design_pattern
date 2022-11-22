# Practical Example #1 -Logging

def logged(function):
    def wrapper(*args, **kwargs):
        value = function(*args, **kwargs)
        with open('logfile.txt','a+') as f:
            fname =  function.__name__
            print(f"{fname} returned value {value}")
            f.write(f"{fname} returned value {value}\n")
        return value 

    return wrapper



@logged
def add(x,y):

    return x + y

add(30,30)


# Practical Example #2 -Timing

import time 


def timed(function):
    def wrapper(*args,**kwargs):
        before = time.time()
        value = function(*args, **kwargs)
        after = time.time()
        fname = function.__name__
        print(f"{fname} took {after - before} seconds to execute")
        return value
    
    return wrapper



@timed
def myfunction(x):
    result = 1
    for i in range(1,x):
        result *=i
    return result


myfunction(10000)

# def mydecorator(function):
#     def wrapper(*args, **kwargs):
#         print("I am decorating your function")
#         function(*args, **kwargs)
    
#     return wrapper




# @mydecorator
# def hello(person):
#     print(f"Hello {person}")






# hello("Cherif")



def secondLogged(func):
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        with open("log.txt", "a+") as f:
            fname = func.__name__
            print(f"{fname} returned the value {value}")
            f.write(f"{fname} returned the value {value}\n")

        return value 
    
    return wrapper




@secondLogged
def product(x,y):
    return x*y


product(20,30)

    
            

