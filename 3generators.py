# Generators 


# for x in range(1,200):
#     print(x**3)

import sys

def mygenerator(n):
    for x in range(n):
        yield x**3
    

values = mygenerator(200000000000)

print(sys.getsizeof(values))

def infinite_sequence():
    result = 1

    while True:
        yield result
        result*=5



val = infinite_sequence()

for i in range(10):
    print(next(val))
