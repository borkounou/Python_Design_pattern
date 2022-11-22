class Singleton:
    instance = None 
    def __new__(cls):
        if cls.instance is None:
            cls.instance = object.__new__(cls)
        return cls.instance



print(object() is object(), Singleton() is Singleton())