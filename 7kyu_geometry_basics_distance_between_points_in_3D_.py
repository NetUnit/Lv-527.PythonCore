import numpy as np
from math import sqrt


# codewars task12 - 'Arithmetic sequence - sum of n elements'- 7kyu KATA
'''
    This series of katas will introduce you to basics of doing geometry with computers.

    Point objects have x, y, and z attributes. For Haskell there are Point data types described with record syntax with fields x, y, and z.

    Write a function calculating distance between Point a and Point b.  
'''


# var1 NON-RELEWANT WITH CODEWARS
# selecting data through space
class Point:
    try:
        a = [15, 10, 5];
        b = [30, 40, 50];
    
        def __init__(self, a=a, b=b):
            self.a = a
            self.b = b

    except ValueError:
        print(-1)
        exit()
    except NameError:
        print(-1)
        exit()

    def distance_between_points(self, a, b):
        try:
            p1 = list(map(float, a))
            p2 = list(map(float, b))
                
            if len(p1) == len(p2) > 0:
                arr = np.array([b, a])
                calc = np.diff(arr, axis = 0)
                # return "The distance between two points is %.6f cm" % sqrt(sum(sum(calc)**2))
                # return "The distance between two points is {0} cm".format(round(sqrt(sum(sum(calc)**2)), 5))
                return f'The distance between two points is {round(sqrt(sum(sum(calc)**2)), 6)} cm'
            else:
                return -1
        except ValueError:
            return None

a = list(map(int, input('Type the coords of the first point, through space: ').split()))
b = list(map(int, input('Type the coords of the first point, through space: ').split()))

instance = Point()
print(instance.distance_between_points(a, b))


# var2 NON-RELEWANT WITH CODEWARS
# selecting data through space
class Point:

    try:
        a = list(map(int, input('Type the coords of the first point, through space: ').split()))
        b = list(map(int, input('Type the coords of the first point, through space: ').split()))
    
        def __init__(self, a=a, b=b):
            self.a = a
            self.b = b

    except ValueError:
        print(-1)
        exit()
    except NameError:
        print(-1)
        exit()

    def distance_between_points(self):
        try:
            p1 = list(map(float, self.a))
            p2 = list(map(float, self.b))
                
            if len(p1) == len(p2) > 0:
                arr = np.array([self.b, self.a])
                calc = np.diff(arr, axis = 0)
                # return "The distance between two points is %.6f cm" % sqrt(sum(sum(calc)**2))
                # return "The distance between two points is {0} cm".format(round(sqrt(sum(sum(calc)**2)), 5))
                return f'The distance between two points is {round(sqrt(sum(sum(calc)**2)), 6)} cm'
            else:
                return -1
        except ValueError:
            return None
            

instance = Point()
print(instance.distance_between_points())


# var3 RELEWANT WITH CODEWARS
def distance_between_points(a, b):
    zipped_list = list(zip((a.x, a.y, a.z), (b.x, b.y, b.z)))

    lst = []
    for a, b in zipped_list:
        a = [(a - b)**2]
        lst += a
            
        # return f'{round(sqrt(sum(lst)), 6)}'
        # return "{0}".format(sqrt(sum(lst)))
        return "%.6f" % sqrt(sum(lst))



