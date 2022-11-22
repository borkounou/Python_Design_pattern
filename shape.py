from abc import ABCMeta, abstractmethod

class IShape(metaclass=ABCMeta):


    @abstractmethod
    def draw():
        "Shape to implement later"


class Rectangle(IShape):

    def draw(self):
        print("Inside Rectangle::draw() method")


class Circle(IShape):
    def draw(self):
        print("Inside Circle::draw() method")


class Square(IShape):
    def draw(self):
        print("Inside Square::draw() method")




class ShapeFactory:

    @staticmethod
    def getShape(shapeType):
        if shapeType==None:
            return None
        elif shapeType=="RECTANGLE":
            return Rectangle()
        elif shapeType=="CIRCLE":
            return Circle()
        elif shapeType =="SQUARE":
            return Square()
        else:
            return None



if __name__ == "__main__":

    shapeFactory = ShapeFactory()
    shape1 = shapeFactory.getShape("RECTANGLE")
    shape1.draw()

    shape2 = ShapeFactory.getShape("CIRCLE")
    shape2.draw()

    shape3 = ShapeFactory.getShape("SQUARE")
    shape3.draw()
        

