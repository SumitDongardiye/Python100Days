# args is used for positional arguments. Tupple is passed
from numpy.ma.core import multiply


def add(*args):    #Pass unlimited values
    summ=0
    for n in args:
        summ+=n

    print(summ)


add(1,2,3,4,5,6)


# kwargs is used for keyword arguments. Dictionary is passed

def calculate(n,**kwargs):
    # for key,value in kwargs.items():
    #     print(key,value)
    n+=kwargs["add"]
    n*=kwargs["multiply"]
    print(n)

calculate(2,add=3,multiply=5)

class Car:
    def __init__(self, **kw):
        self.make=kw["make"]
        self.model=kw["model"]
        self.color=kw["color"]
        self.seats=kw["seats"]

my_car=Car(make="Nissan",model="GT-R",color="Blue",seats=2)
print(my_car.make)