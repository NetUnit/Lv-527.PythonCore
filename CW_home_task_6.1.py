import numpy as np
import math
import time
from math import dist
#from scipy.spatial import distance

# codewars task1 'Distance between two points'- SoftServe6 - Lesson6

#1.1 Return the distance between the points (2 coords)

def distance(x1, y1, x2, y2): 
    distance = ( (x2 - x1)**2 + (y2 - y1)**2 ) ** (1/2)
    return round (distance, 2)
    
#RELEVANT WITH CODEWARS
#https://prnt.sc/uhoxmn

#1.2 Return the distance between the 2 points (3 coords). (SIMILAR KATA with N-points)

'''
    Formula = ((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1))** 0.5


    using zip+lc+formula:
        1) зазіпує дані зі списку/тюпла [x1, y1, z1], [x2, y2, z2] = [(x2 - x1), (y2 - y1), (z2 - z1)]
            zip даних виглядає наступним чином <zip object at 0x7f0353b52280> - HEX data
            щоб витягнути ці дані потрбіно їх обгорнути в list/tuple/set

        2) виконаємо математичний розрахунок (x2-x1)**2 для кожного аргумента в зіпованому списку
            за допомогою list comprehension
            (x2 - x1)**2 = [(x2-x1)**2 for x2, x1 in zipped_list]

            Отримаємо дані за наступним списком: [a, b, c] (де a = (x2 - x1)**2)

        3) Далі ці дані потрбіно просумувати та взяти з них кв. корінь згідно з формулою та використавши модуль math
            math.sqrt(sum[a, b, c]) де sum(a, b, c) - звичайний метод суми списку


        Розв'язати задачу можнатакож за допомогою модуля numpy.
        !!! у випадку з формулою  np.linalg.norm(p1-p2):

            !!! список потрібно конвертувати в np.array() - дізнатис ящо таке np array

            np.array(p1).astype(int) # тільки для натуральних чисел > 0,
            якщо вводитимуться від'ємні числа - astype(int) потрібно забрати

'''

# using zip+lc+formula


def dist(p1, p2):
    if len(p1) == len(p2):

        #1) дія1
        # [x1, y1, z1], [x2, y2, z2] = [(x2 - x1), (y2 - y1), (z2 - z1)]
        zipped_list = list(zip(p1, p2))
        #return zip(p1, p2)

        #2) дія2
        calculated_zipped_list = [(a-b)**2 for a, b in zipped_list]
        #return calculated_zipped_list

        #3) дія3
        calculation = math.sqrt(sum(calculated_zipped_list))
        return round(calculation, 3)

    else:
        return -1


p1 = list(map(int, input('Type the coords of the first point, through space: ')))
p2 = list(map(int, input('Type the stcoords of the first point, through space: ')))

print(dist(p1, p2))

# using numpy module $ linear algebra formula


def dist2(p1, p2):
    # p1, p2 # are arrays of (x1, y1, z1....), (x2, y2, z2, ...)
    if len(p1) == len(p2):
        calc_dist = np.linalg.norm(p1-p2)  # np.array(p1)-np.array(p2) as an option
        return calc_dist
    else:
        return -1


p1 = list(map(int, input('Type the coords of the first point, through space: ')))
p1 = np.array(p1).astype(int) # увага тільки для натуральних чисел > 0, якщо вводитимуться від'ємні числа - astype(int) потрібно забрати
#print(type(p3))

p2 = list(map(int, input('Type the coords of the first point, through space: ')))
p2 = np.array(p2).astype(int)

#print(type(p4))
print(dist2(p1, p2))


# using the math module and dist formula


def dist3(p1, p2):
    if len(p1) == len(p2):                  # p1, p2 # are arrays of (x1, y1, z1....), (x2, y2, z2, ...)
        return math.dist(p1, p2)
    else:
        return -1


p1 = tuple(map(int, input('Type the coords of the first point, through space: ')))
p2 = tuple(map(int, input('Type the stcoords of the first point, through space: ')))

print(round(dist3(p1, p2), 3))


# using the math module and zip


def dist4(p1, p2):
    if len(p1) == len(p2):
        # якщо всі попередні дії записати однією формулою
        return math.sqrt(sum((a - b)**2 for a, b in zip(p1, p2)))


p1 = tuple(map(int, input('Type the coords of the first point, through space: ')))
p2 = tuple(map(int, input('Type the stcoords of the first point, through space: ')))

print(round(dist4(p1, p2), 3))


# using the cycle for to implement the formula (non-relevant with codewars)


#def dist(p1, p2):
    #if len(p1) == len(p2):
        #united_lst = list(zip(p1, p2))

	#for x in united_lst:
	#sum = 0

	#for a,b in x:
	#sum = a - b

	#return united_lst

        #return math.sqrt(sum(lst))

    #else:
        #return -1


#p1 = list(map(int, input('Type the coords of the first point, through space: ')))
#p2 = list(map(int, input('Type the coords of the first point, through space: ')))


#p1 = list(map(int, input('Type the coords of the first point, through space: ')))
#p2 = list(map(int, input('Type the coords of the first point, through space: ')))






















def distance_(p1, p2): 

     if len(p1) == len(p2):
		return round ( math.sqrt ( (x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2 ), 2 )

	else:
		return -1 

x1 = int(input ('Type the coord x1 of the first point: '))
y1 = int(input ('Type the coord y1 of the first point: '))
z1 = int(input ('Type the coord z1 of the first point: '))


x2 = int(input ('Type the coord x2 of the first point: '))
y2 = int(input ('Type the coord y2 of the first point: '))
z2 = int(input ('Type the coord z2 of the first point: '))

#lst1 = [str(x) for x in str(x1)] + [str(x) for x in str(y1)] + [str(x) for x in str(z1)] # LC is bad when it is a two digit symbol
#lst2 = [str(x) for x in str(x2)] + [str(x) for x in str(y2)] + [str(x) for x in str(z2)] # LC is bad when it is a two digit symbol

lst1 = [] # Pomeranska T. way to create lists
lst1.append(x1)
lst1.append(y1)
lst1.append(z1)


lst2 = []
lst2.append(x2)
lst2.append(y2)
lst2.append(z2)

p1 = list(np.array(lst1).astype(int)) # array of integers # p1 and p2 should be given as arrays
p2 = list(np.array(lst2).astype(int)) # array of integers

print (p1)
print (p2)

print (type(p1))
print (type(p2))


print (distance_(p1, p2))

# NON-RELEVANT WITH CODEWARS - https://prnt.sc/uf81ys (EOF WHEN READING THE LINE)
# 16.09 - TRY TO USE 'ZIP' FOR CALCULATION
# # array - множина, масив (матриця)








