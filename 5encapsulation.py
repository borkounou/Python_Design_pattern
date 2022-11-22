

class Person:
    def __init__(self,name, age, gender):
        self.__name = name
        self.__age = age 
        self.__gender = gender
        
    
    @property
    def Name(self):
        return self.__name
    @Name.setter
    def Name(self,value):
        self.__name = value


    @property
    def Age(self):
        return self.__age

    
    @Age.setter
    def Age(self, value):
        self.__age = value

    @property
    def Gender(self):
        return self.__gender

    
    @Gender.setter
    def Gender(self, value):
        self.__gender = value

    @staticmethod
    def mymethod():
        print("Hello world!")
        return 10



p = Person("Cherif", 20, "M")
print(p.Name)

p.Name = "Hassan"
print(p.Name)

Person.mymethod()
s = p.mymethod()
print(s)