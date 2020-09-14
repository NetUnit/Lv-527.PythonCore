import time
import numpy as np
import random

# classwork 25.08 task (4.1-4.5) - SoftServe4 - Lesson4

#Роздрукувати всі парні числа менші 100

# 4.1.1 # виведе парні цифри від 0 (використовуючи цикл while)
#OPTION1

a = 0 # цикл з основою на додаванні 2ки до стартового числа 0
while a <= 100:
	print (a)
	a += 2 # a = a + 2
	

# 1.1.2 # виведе всі парні цифри від 0 (використовуючи цикл for)
#OPTION2

for a in range (1, 100): # 1 - число початку діапазону, 100 - число кінця діапазону (не включаючи 100)
	a += 1
	if (a % 2) == 0:
		print (a)
	else:
		pass
	

###########################################################################################################################################

#Роздрукувати всі непарні числа менші 100. (написати два варіанти коду: один використовуючи оператор continue, а інший без цього оператора).
# 4.2.1 # із застосуванням 'сontinue' всі непарні числа
#OPTION1

a = 0
while a <= 99: # так як ми виводимо непарні числа то останнім непарним є - 99
	a += 1 
	if (a % 2) == 0: # ділення по модулю на парне число - буде дорівнювати 0 # далі нулі пропускаємо використовуючи continue
		continue # пропустить всі парні числа
	print (a)

# 4.2.2 із застосуванням 'сontinue' всі парні числа
#Example2

a = 0 
while a <= 100: # останнім парним є - 99
	a += 1 
	if (a % 2) == 1: # # ділення по модулю на парне число - буде дорівнювати 1 # далі одиниці пропускаємо використовуючи continue
		continue # пропустить всі непарні числа
	print (a)


# 4.2.3 без застосування 'сontinue' всі непарні числа (цикл For)
#OPTION2

for a in range(1, 100, 2): # 1 - початок діапазону, 100 -кінець діапазону (не включаючи 100), 2 - хід діапазону
	print (a)


# 4.2.4 із застосуванням від'ємного значення (всі непарні) (цикл For)
#Example2

for a in range(2, 101):
	a = a - 1
	if (a % 2) == 1:
		print (a)
	else:
		pass

# 4.2.5 із застосуванням від'ємного значення (всі непарні) (цикл For)
#Example3

for a in range(3, 102):
	a = a - 2
	if (a % 2) != 0:
		print (a)
	else:
		pass

# 4.2.6 із формуванням зі списку (всі непарні)
#Example4 

numbers = list ( range ( 1, 100, 1 ))
numbers_slice = numbers [:100:2] 

tpl_lst = tuple ( numbers_slice )

strings = [str(integer) for integer in tpl_lst] ### converting to a string (from TUPLE∕LIST∕CORTEGE∕DICTIONARY)
a_string = " ".join(strings)
an_integer = str(a_string)

print ( an_integer ) # видасть набір чисел в форматі кортежа

###########################################################################################################################################


# 4.3.1 Check the list if it contains odd numbers - Using 'break' operator (iterating each number in the list)

num = input ('Type some digits: ')
int_lst = [int(x) for x in str(num)] # using list comprehension to convert number to the list of integers
print (int_lst) # printing a list
 
for num in int_lst: 
    # checking condition 
	if (num % 2) == 1: 
		print (num)
		# double condition allows 
	elif (num % 2) != 1:
		pass
	else:
		break # using break

# 4.3.2 Check the list if it contains even numbers - Using 'break' operator
# Example 2 #OPTIONAL# NOT NECESSARY

time.sleep(1)
print ('...')

# iterating each number in the list 
def option2():
	for num in int_lst: 
	    # checking condition 
		if (num % 2) != 1: 
			print (num)
			# double condition allows 
		elif (num % 2) == 1:
			pass
		else:
			break 

check_odd_num = input ('Do U want to check even numbers in the list?: ')
yeslist = ['Yes', 'yes', 'sure', 'definately']
if check_odd_num in yeslist:
	print (option2())
else:
	pass


# 4.3.3 Check list if it contains odd numbers - Using 'break' operator (Liybov Koliasa example)
#Example3 #OPTIONAL# NOT NECESSARY

num_odd = False

for i in int_lst:
	if (i % 2) != 0:
		num_odd = True
		break
if num_odd:
	print ('There is an odd number here')
else:
	print ('There is only even numbers here')


###########################################################################################################################################

#4.4.1 Create the list of integers, then change data type of this list to decimal using float (SHORTEST WAY)
  
# list of numbers  

numbers = list ( range ( 1, 100)) # creating the list

print (numbers) # will print the numbers in the 'list' format

for i in numbers: # using 'for' cycle to convert each element in the list to float
	print (float(i))

#4.4.2 Create the list of integers ('that user may potentially type', then change data type of this list to decimal using float

num = input ('Trial#2, Type some digits: ')
int_lst = [int(x) for x in str(num)] # using the 'LC' to convert number to the list of integers
print (int_lst) # printing a list
print (type(int_lst)) # checking the data type of created object

for i in int_lst:
	print (float(i))

#4.4.3 Create the list of integers ('that user may potentially type', then create a float list from digits using the the 'LC'

num = input ('Trial#3, Type some digits: ')

fl_list = [float(x) for x in num] # accurately create the list of floats
print (fl_list)

#4.4.4 Using the 'map' function

num = input ('Trial#4, Type some digits: ')
int_lst = [int(x) for x in str(num)] # creating the list

fl_lst = list(map(float, int_lst)) # the same part using the single function

print (fl_lst)

#4.4.5 Using 'numpy' module to convert a list directly to a floating array or a matrix

num = input ('Trial#5, Type some digits: ') 

int_lst = [int(x) for x in str(num)] # beforehand we need to convert a regular digit to a list of integers usng the 'LC'

list_float = list(np.array(int_lst).astype(float)) # convert the list of integers to the list of floats
#list_float = np.array(int_lst) + .0 # Another option to do the task - # If we want to convert the integer array to a floating array then add 0 to it

print(type(list_float), type(list_float[0])) # displaying the type as a list of strings

print (list_float)

# list_int = np.array(int_lst) # This is a numpy integer array created

#4.4.6 Using 'random' module to create the list of random digits

for (i) in range(1): # 1 generating 1 time

	num_rand = random.randint(1000000000, 10000000100) #generating a regular 10digit number from 1000000000 to 100000000100

int_lst = [int(i) for i in str(num_rand)] # using 'LC' to create a list of integers
print (type(int_lst))

list_float = list(np.array(int_lst).astype(float))
print(list_float)


###########################################################################################################################################

#5.1.1 Create the list of Fibonacci Numbers using cycle (while, for) up to 13

# Fn = Fn-1 + Fn-2
# F0 = 0, F1 = 1

# Function to create Fibonacci number using condition and formula

n = int(input ('Trial#1. Type the Fibonacci number:')) 

def Fibonacci(n): 
    if n<0: 
        print("Incorrect input") 
    # First Fibonacci number is 0 
    elif n == 1: 
        return 0
    # Second Fibonacci number is 1 
    elif n == 2: 
        return 1
    # The third Fibonacci number is 1
    else: 
        return Fibonacci(n-2)+Fibonacci(n-1) 

print(Fibonacci(n)) 

#5.1.2 Create the list of Fibonacci Numbers using not efficient recursive function

time.sleep(2)

r = int(input ('Trial#2. Seelct the Fibonacci range:'))

def rec_fib(n): # recursion function 
    '''inefficient recursive function as defined, returns Fibonacci number - works only up to 30''' 
    if n > 1:
        return rec_fib(n-1) + rec_fib(n-2) # described the formula Fn = Fn-1 + Fn-2 through function
    return n

for i in range(r):
    print(rec_fib(i))

time.sleep(2)

#5.1.3 Create the list of Fibonacci Numbers using cycle (while)
# Program to display the Fibonacci sequence up to n-th term

nterms = int(input("Trial#3. How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence up to", nterms, ":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1



















