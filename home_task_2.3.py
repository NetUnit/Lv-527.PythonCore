import time

# task3 - SoftServe#3 - Lesson3

#CHANGE A VALUE OF VARIABLE NOT INCLUDING THE 3RD VARIABLE

#3.1 Simple replacement  

var_1 = 100
var_2 = 200

print (var_1, ' - var_1')
print (var_2, ' - var_2')

var_1, var_2 = var_2, var_1

print (var_1, ' - var_1')
print (var_2, ' - var_2')


#3.2 Change a value of variable not including the 3rd variable
# Example2

variable_1 = 25
variable_2 = 'Text1 '

print ('Our variables are: ' + str (variable_1) + ' and ' + str (variable_2))

def change1(x):
	x = int (input ( 'add some digit: '))
	return variable_1 + int(x)

def change2(y):
	y = str (input ( 'add some text to Text1: '))
	return variable_2 + str(y)

time.sleep(1)

print (change1('x'))
print (change2('y'))

#ЗМІНА ЗНАЧЕНЬ ЗМІННИХ 

# 3.3 change a value of variable using replace() method (just replace the value)
# Example3


variable_1 = 'Text1'
variable_2 = 'Text2'
print (variable_1)
print (variable_2)

time.sleep(1)

variable_2 = variable_2.replace ('Text2', 'Text1')
variable_1 = variable_1.replace ('Text1', 'Text2')

print (variable_1)
print (variable_2)

#ЗАМІНА ЗНАЧЕНЬ з replace





