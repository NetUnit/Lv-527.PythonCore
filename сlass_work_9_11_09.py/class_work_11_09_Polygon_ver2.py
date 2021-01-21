import numpy as np
from math import sqrt
import copy
import time

# classwork1 'class Polygon' - SoftServe#9 - Lesson9 OOP


'''
    In this version we neet to set-up sides, 
    i order to execute the calculations.

    Single class is a separate geometrical figure
'''


# var3
class Polygon:

    # набір сторін - контейнер під сторони
    def __init__(self, num_of_sides):
        self.num_of_sides = num_of_sides
        self.sides = [0 for i in range (num_of_sides)]
    
    # цей блок буде виводити кількість інпутів стільки разів скільки буде сторін у фігури
    # інпути не потрбіно буде вводити окремо до кожної сторони
    # input() - введення кожної сторони
    # self.sides - унаслідується від __init__
    def set_sides(self):
        self.sides = [float(input(f'Enter the side #{str(i+1)}: '))
                                 for i in range(self.num_of_sides)]
    # вивести на екран - попередній результат введений користувачем (так як у нашому варіанті з Polygon)
    def display_sides(self):
        for i in range(self.num_of_sides):
            print(f'Side {i+1} is {self.sides[i]}')


#instance = Polygon(4)   
#print(instance.set_sides())
#print(instance.display_sides())

class Triangle(Polygon):

    # передаємо __init__ одного класу в інший Polygon.__init__
    def __init__(self):
        Polygon.__init__(self, 3)
    
    def find_area(self):
        a, b, c = self.sides
        # calculation of semi-perimeter
        s = (a + b + c) / 2
        return s
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print(f'The area of the triangle is {area}')
    

instance = Triangle()
instance.set_sides()

print(instance.find_area())


class Rectangle(Polygon):

    # передаємо __init__ одного класу в інший Polygon.__init__
    def __init__(self):
        Polygon.__init__(self, 2)
    
    def find_area(self):
        a, b = self.sides
        # calculation of semi-perimeter
        s = a * b
        return(f'The area of the rectangle is {s} cm2')
    

instance = Rectangle()

instance.set_sides()
instance.display_sides()
print(instance.find_area())
