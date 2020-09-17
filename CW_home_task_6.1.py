import numpy as np
import math
import time

# codewars task1 'Distance between two points'- SoftServe6 - Lesson6

#1.1 Return the distance between the points (2 coords)

def distance(x1, y1, x2, y2): 
    distance = ( (x2 - x1)**2 + (y2 - y1)**2 ) ** (1/2)
    return round (distance, 2)
    
#RELEVANT WITH CODEWARS
#https://prnt.sc/uhoxmn

#1.2 Return the distance between the 2 points (3 coords). (SIMILAR KATA)

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








