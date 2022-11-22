


class Vector:
    def __init__(self, x,y) -> None:
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x +other.x, self.y + other.y)

    
    def __mul__(self, other):
        return Vector(self.x * other.x, self.y*other.y)


    def __repr__(self):
        return f"X:{self.x}, Y:{self.y}"

    def __len__(self):
        return 10


    def __call__(self):
        print("Hello! I was called!")




class Calculator:
    def __init__(self,x):
        self.x =x
    def __add__(self, other):
        return Calculator(self.x+other.x)
    def __repr__(self):
        return f"{self.x}"

    # def __del__(self):
    #     print("I am destroyed")

        

# v1 = Vector(10,20)
# v2 = Vector(50,60)

# v3 = v1 *v2

# print(v3.y)
# print(v3)

# print(len(v3))


i = Calculator(20)
j = Calculator(30)
k = i+j
print(k)
        