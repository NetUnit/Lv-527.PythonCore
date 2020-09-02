import numpy as np # https://linuxconfig.org/install-numpy-on-ubuntu-20.04-bionic-beaver-linux - tutorial
import random

# classwork task4- SoftServe#4 - Lesson4

# 'List comprehension' - 'LC' in further

#1.1 Create the list of integers, then change data type of this list to decimal using float
  
# list of numbers  

numbers = list ( range ( 1, 100)) # creating the list

print (numbers) # will print the numbers in the 'list' format

for i in numbers: # using 'for' cycle to convert each element in the list to float
	print (float(i))

#1.2 Create the list of integers ('that user may potentially type', then change data type of this list to decimal using float

num = input ('Trial#2, Type some digits: ')
int_lst = [int(x) for x in str(num)] # using the 'LC' to convert number to the list of integers
print (int_lst) # printing a list
print (type(int_lst)) # checking the data type of created object

for i in int_lst:
	print (float(i))

#1.3 Create the list of integers ('that user may potentially type', then create a float list from digits using the the 'LC'

num = input ('Trial#3, Type some digits: ')

fl_list = [float(x) for x in num] # accurately create the list of floats
print (fl_list)

#1.4 Using the 'map' function

num = input ('Trial#4, Type some digits: ')
int_lst = [int(x) for x in str(num)] # creating the list

'''fl_lst = map(float, int_lst)
fl_lst2 = list(fl_lst)'''

fl_lst = list(map(float, int_lst)) # the same part using the single function

print (fl_lst)

#1.5 Using 'numpy' module to convert a list directly to a floating array or a matrix

num = input ('Trial#5, Type some digits: ') 

int_lst = [int(x) for x in str(num)] # beforehand we need to convert a regular digit to a list of integers usng the 'LC'

list_float = list(np.array(int_lst).astype(float)) # convert the list of integers to the list of floats
#list_float = np.array(int_lst) + .0 # Another option to do the task - # If we want to convert the integer array to a floating array then add 0 to it

print(type(list_float), type(list_float[0])) # displaying the type as a list of strings

print (list_float)

# list_int = np.array(int_lst) # This is a numpy integer array created

#1.6 Using 'random' module to create the list of random digits

for (i) in range(1): # 1 generating 1 time

	num_rand = random.randint(1000000000, 10000000100) #generating a regular 10digit number from 1000000000 to 100000000100

int_lst = [int(i) for i in str(num_rand)] # using 'LC' to create a list of integers
print (type(int_lst))

list_float = list(np.array(int_lst).astype(float))
print(list_float)





