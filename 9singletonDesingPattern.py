from abc import ABCMeta, abstractstaticmethod

class IPerson(metaclass=ABCMeta):

    @abstractstaticmethod
    def print_data():
        """Implement in child class"""



class PersonSingleton(IPerson):

    __instance = None

    @staticmethod
    def get_instance():
        if PersonSingleton.__instance ==None:
            PersonSingleton('Default Name',0)
        return PersonSingleton.__instance
    
    def __init__(self, name, age):
        if PersonSingleton.__instance!=None:
            raise Exception("Singleton cannot be instantiated more than one")
        else:
            self.name = name
            self.age = age
            PersonSingleton.__instance =self

    
    @staticmethod
    def print_data():
        print(f"Name:{PersonSingleton.__instance.name}\n Age:{PersonSingleton.__instance.age}")
            



p = PersonSingleton("Cherif",22)
print(p)
p.print_data()