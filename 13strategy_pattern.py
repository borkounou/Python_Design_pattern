from abc import ABCMeta, abstractmethod

class IStrategy(metaclass=ABCMeta):

    @abstractmethod
    def doOperation(self, num1, num2):
        pass



class OperationAdd(IStrategy):

    def doOperation(self, num1, num2):
        return num1 + num2


class OperationSubtract(IStrategy):
    def doOperation(self, num1, num2):
        return num1 -num2



class OperationMultiply(IStrategy):
    def doOperation(self, num1, num2):
        return num1 * num2


class Context:
    def __init__(self,strategy:IStrategy):
        self.__strategy = strategy

    
    def executeStrategy(self,num1,num2):
        return self.__strategy.doOperation(num1,num2)



# class StategyPatternDemo:
#     def main(self):
#         context = Context(OperationAdd())
#         print(f"10 + 5 = {context.executeStrategy(10,5)}")

def calculator(num1,num2, operation):
    if operation ==1:
        return num1 +num2
    elif operation==2:
        return num1 - num2
    elif operation==3:
        return num1* num2
    else:
        return 0


if __name__ == "__main__":

    context = Context(OperationAdd())
    print(f"10 + 5 = {context.executeStrategy(10,5)}")

    


