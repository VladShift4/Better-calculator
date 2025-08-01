import math

def fact(num_1):
    return math.factorial(num_1)

def sqr(num_1):
    try:
        math.sqrt(num_1)
    except ValueError:
        print("You can`t find a square root from a negative number")
    return math.sqrt(num_1)


def logar(num_1, num_2):
    try:
        math.log(num_1, num_2)
    except ValueError:
        print("Basis can`t be less than 0!")
    return math.log(num_1, num_2)

def rad(num_1):
    return math.radians(num_1)

def cosin(num_1):
    return math.cos(num_1)

def arccosin(num_1):
    return math.acos(num_1)

def sin(num_1):
    return math.sin(num_1)

def arcsin(num_1):
    return math.asin(num_1)

def tangens(num_1):
    return math.tan(num_1)

def arctangens(num_1):
    return math.atan(num_1)