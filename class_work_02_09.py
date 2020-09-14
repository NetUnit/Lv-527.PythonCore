import math
import time


#classwork2 02.09 - SoftServe#6 - Lesson6

#1.1 "Arithmetic mean" function 

def arithmetic(x):
	arith_lst = [ int(i) for i in str(x) ]
	print (type(arith_lst))
	return sum(arith_lst)/len(arith_lst)

num = int(input ('Type the number: '))
print ( 'The arithmetic mean of these digits is: ' + str(arithmetic(num)) )

#2.1 Function that creates the list of integers, determine 'max' and 'min'. Use !!!DOCSRTRING!!!

def max(x, y):

	# docstring included
	''' In this peace of code we are going to make a simple thing:
		1) compare 2 variables
		2) return biger value with 'return' operator

		Lets get started :) 
	 ''' 	 
	if x>y:
		return (x) 
	else:
		return (y)
x = input ('Select the first integer U want to compare: ')
y = input ('Select the second integer U want to compare: ')

print( 'The biger number is: ' + str(max(x, y)) )

time.sleep(1)

print( max.__doc__) # docstring info will arise

#3.1 Create a program that will count the surface area of rectangular, traingle or cyrcle figure, according to customer's selection 
# rectang

def rectang():
	a = int(input (' Enter the side lenght: '))
	b = int(input (' Enter the side width: '))
	s = a * b
	
	return 'The square of a rectang is: {}m2'.format(s)

# triangle
def triangle():
	 
	a = int(input ('Please enter the length of the first side: '))
	b = int(input ('Please enter the length of the second side: '))
	c = int(input ('Please enter the length of the third side: '))

	p = 0.5 * (a + b + c) 
	s = math.sqrt ( p*(p-a) + p*(p-b) + p*(p-c) )

	return 'The square of a triangle is: {}m2'.format(s)

# circle
def circle():
	r = int(input ('Please enter the radius of the circle: '))
	s = (math.pi) * (r**2)
	#round_s = round(s, 2)
	
	return 'The square of a circle is: {} m2'.format(round(s, 2))


selection = input ('What type of a geometrical figure do U want to identify? ')	
#select_lst = ['Circle', 'circle', 'Triangle', 'triangle', 'Rectang', 'rectang']

if selection == 'Rectang' or selection == 'rectang':
	print (rectang())

elif selection == 'Triangle' or selection == 'triangle':
	print (triangle())

elif selection == 'Circle' or selection == 'circle':
	print (circle())
else:
	time.sleep(1)
	'...'
	time.sleep(1)
	print ('The program is over')


#4.1 Написати функцію, яка обчислює кількість символів, які входять в задану стрічку

def num_symb (x):

	x = input ('Please type the \'str\': ') 
	return 'The length of this \'str\' is: ' + str(len(list(x))) + ' letters' # lastly without 'LC'

print (num_symb(x))
															



