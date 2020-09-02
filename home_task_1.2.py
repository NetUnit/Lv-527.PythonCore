import time

# hometask2 - SoftServe1 - Lesson1

time.sleep(1)
print ('We are going to execute some code ')
time.sleep(1)
print ('...')

def calculations():

	c = input ( 'Please select the \'a\' variable: ')
	a = int (c) # we can put except here to catch a ValueError in the case when user not type digit 
	
	d = input ( 'Please select the \'b\' variable: ')
	b = int (d)

	SUM = a + b
	MINUS = a - b
	MULTIPLICATION = a * b
	DIVISION = a / b
	SQRT = a ** b

	output = 'Result: ' + str ( SUM ) + ' ' + str ( MINUS ) + ' ' + str ( MULTIPLICATION ) + ' ' + str ( DIVISION ) + ' ' + str ( SQRT ) 

	print ( output )

calculations()



