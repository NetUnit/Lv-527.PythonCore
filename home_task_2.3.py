import time

# hometask3 - SoftServe#3 - Lesson3

# task3 - CHANGE A VALUE OF VARIABLE NOT INCLUDING THE 3RD VARIABLE - USING INPUT

#3.1 using input+

variable_1 = 25
variable_2 = 'Programiz '

print ('Our variables are: ' + str (variable_1) + ' and ' + str (variable_2))

def change1(x):
	x = int (input ( 'add some digit: '))
	return variable_1 + int(x)

def change2(y):
	y = str (input ( 'add some text: '))
	return variable_2 + str(y)

time.sleep(1)

print (change1('x')) # something should be in brackets as an argument
print (change2('y'))

#3.2 change a value of variable not including the 3rd variable not using input

def change1(x):
	return variable_1 + int(x)

def change2(y):
	return variable_2 + str(y)

time.sleep(1)

print (change1('250')) 
print (change2('+100500'))

#OPTIONAL # '3.2' is not necessary

# 3.3 change a value of variable using replace() method

variable_1 = '25'
variable_2 = 'Programiz '
time.sleep(1)

print(variable_2.replace ('r', '\'r\''))

# reverse replacement

time.sleep(1)
print ('Now we will put variables in the reverse order: ')
time.sleep(2)

print('variable_1: - ' + variable_1.replace ('25', 'Programiz'))
print('variable_2: - ' + variable_2.replace ('Programiz', '25'))

#OPTIONAL # '3.3' is not necessary





