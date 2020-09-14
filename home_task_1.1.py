import time

# hometask1 - SoftServe1 - Lesson1 

#1.1.1 Create a function that outputs: name, age, location

name = input ( 'What is your name?: ')
print ('Your name is: ' + name ) 

age = input ( 'What is your age: ')
print ('Your age is: ' + age ) 

location = input ( 'What is your location: ')
print ( "Your location is: " + location ) 

#1.1.1 

time.sleep(1)
print ('...')
time.sleep(1)
print ('...loading...')
time.sleep(1)
print ('...')
time.sleep(1)
print ('Example2: ')

name = input ( 'What is your name?: ')
age = input ( 'What is your age: ')
location = input ( 'What is your location: ')

def function_name():
	time.sleep(1)
	return ('Your name is: ' + name )
print ( function_name())

def function_age():
	time.sleep(1)
	return ('Your age is: ' + age )
print ( function_age ())

def function_location(x): # using 'x' variable which was then trasferred to the 'output1' function 
	time.sleep(1)
	# x = input ( 'What is your location: ')
	return 'Your location is: ' + x
	
output = function_location
output1 = output ( location )
print ( output1 )

# Example#2
