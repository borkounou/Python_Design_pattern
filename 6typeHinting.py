# mypy

def myfunction(myparameter:int)->str:
    print(myparameter)
    return f"{myparameter +5}"


def otherfunction(otherparamater:str):
    print(otherparamater)


def dosomething(param:list[int]):
    print(param) 



otherfunction(myfunction(20))

list_of_integer = [2,3,5,5,6,6]
list_of_char = ['A', 'B', 'C']

dosomething(list_of_integer)
myfunction(5)