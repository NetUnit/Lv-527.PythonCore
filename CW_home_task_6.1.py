import numpy as np
import math
import time
from math import dist
from math import sqrt
import numpy as np
#from scipy.spatial import distance

# codewars task1 'Distance between two points'- SoftServe6 - Lesson6

# 1.1 Return the distance between the points (2 coords)


def distance(x1, y1, x2, y2):
    distance = ((x2 - x1)**2 + (y2 - y1)**2) ** (1/2)
    return round(distance, 2)


# RELEVANT WITH CODEWARS
#  https://prnt.sc/uhoxmn

# 1.2 Return the distance between the 2 points (3 coords). (SIMILAR KATA with N-points)



'''
    Formula = ((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1))** 0.5 

    using zip+lc+formula:
        1) will create a zipped tuple [x1, y1, z1], [x2, y2, z2] = [(x1 - x2), (y1 - y2), (z1 - z2)] 
            data from zip wrpapper is retrieved by  list/tuple/set <zip object at 0x7f0353b52280>
    
        
        2) arithmetic calculation execution (x1-x2)**2 for each of the elements in a tuple 
            through the list comprehension, iteration or lambda
            (x1 - x2)**2 = [(x1-x2)**2 for x2, x1 in zipped_list]

            We'll the next object: [a, b, c] (де a = (x2 - x1)**2)

        3) Getting sum() (built-in function) of the list elements via math module
            math.sqrt(sum[a, b, c]) where sum(a, b, c) -

        Also we can use numpy module to resolve this task.
        
        !!! In the case with np.linalg.norm(p1-p2) formula: 
            list should be converted into np.array()

            np.array(p1).astype(int) # only for the regular digits > 0, 
            in the case of irregular digits - astype(int) should be removed
'''

'''
# var1 - using zip+lc+formula
def dist(p1, p2):
    if len(p1) == len(p2):

        # 1) action1
        # [x1, y1, z1], [x2, y2, z2] = [(x1 - x2), (y1 - y2), (z1 - z2)]
        zipped_list = list(zip(p1, p2))
        # return zip(p1, p2)

        # 2) action2
        calculated_zipped_list = [(a-b)**2 for a, b in zipped_list]
        # return calculated_zipped_list

        # 3) action3
        calculation = math.sqrt(sum(calculated_zipped_list))
        return round(calculation, 3)

    else:
        return -1


p1 = list(map(int, input('Type the coords of the first point, through space: ')))
p2 = list(map(int, input('Type the stcoords of the first point, through space: ')))
print(dist(p1, p2))


# var2 using numpy module & linear algebra formula
def dist2(p1, p2):
    # p1, p2 # are arrays of (x1, y1, z1....), (x2, y2, z2, ...)
    if len(p1) == len(p2):
        # np.array(p1)-np.array(p2) as an option
        calc_dist = np.linalg.norm(p1-p2)
        return calc_dist
    else:
        return -1


p1 = list(map(int, input('Type the coords of the first point, through space: ')))
# увага тільки для натуральних чисел > 0, якщо вводитимуться від'ємні числа - astype(int) потрібно забрати
p1 = np.array(p1).astype(int)
# print(type(p3))

p2 = list(map(int, input('Type the coords of the first point, through space: ')))
p2 = np.array(p2).astype(int)

# print(type(p4))
print(dist2(p1, p2))


# var3 using the math module and dist formula
def dist3(p1, p2):
    if len(p1) == len(p2):  # p1, p2 # are arrays of (x1, y1, z1....), (x2, y2, z2, ...)
        return math.dist(p1, p2)
    else:
        return -1


p1 = tuple(map(int, input('Type the coords of the first point, through space: ')))
p2 = tuple(map(int, input('Type the stcoords of the first point, through space: ')))

print(round(dist3(p1, p2), 3))


# var4 using the math module and zip
def dist4(p1, p2):
    if len(p1) == len(p2):
        # single formula scenario
        return math.sqrt(sum((a - b)**2 for a, b in zip(p1, p2)))


p1 = tuple(map(int, input('Type the coords of the first point, through space: ')))
p2 = tuple(map(int, input('Type the stcoords of the first point, through space: ')))

print(round(dist4(p1, p2), 3))


# var5 using the loop 'for' + simple iteration
def distance(p1, p2):
    try:
        if len(p1) == len(p2) > 0:
            zipped_list = list(zip(p1, p2))

            lst = []
            for a, b in zipped_list:
                a = [(a - b)**2]
                lst += a

                # var2
                #a = (a - b)**2
                # lst.append(a)
                # print(lst)

            solution = sum(lst)

            return sqrt(solution)

        else:
            return -1

    except ValueError:
        return


p1 = list(
    map(int, input('Type the coords of the first point, through space: ').split()))
p2 = list(
   map(int, input('Type the stcoords of the first point, through space: ').split()))
print(dist(p1, p2))


# var6 using diff() method to operate arrays
def distance_between_points(p1, p2):
    try:
        p1 = list(map(float, p1))
        p2 = list(map(float, p2))

        if len(p1) == len(p2) > 0:
            # arrays should be put in a reverse order
            arr = np.array([p1, p2])
            calc = np.diff(arr, axis=1)
            return roundsqrt(sum(sum(calc)**2))
        else:
            return -1
    except ValueError:
        return None


p1 = list(
    map(int, input('Type the coords of the first point, through space: ').split()))
p2 = list(
    map(int, input('Type the stcoords of the first point, through space: ').split()))
print(distance_between_points(p1, p2))
'''

# var7 using 2 different Classes
class Point:

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
    
    def __str__(self):
        return '%d, %d, %d' % (self.x, self.y, self.z) # без str - c не роздрукується
    
    def __add__(self, other):
        x = (self.x - other.x)**2
        y = (self.y - other.y)**2
        z = (self.z - other.z)**2
        return Point(x, y, z)


a = Point(100, 100, 20)
b = Point(2, 4, 6)


class Calculation():
    def distance_between_points(self, c):
        return 'The distance between two points is: %.5f cm' % sqrt(c.x + c.y + c.z)


c = a + b
instance = Calculation()
print(instance.distance_between_points(c))
