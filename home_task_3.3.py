import time

# task4 - SoftServe#4 - Lesson4
  
# creating the list of numbers 

num = input ('Type some digits: ')
int_lst = [int(x) for x in str(num)] # using list comprehension to convert number to the list of integers
print (int_lst) # printing a list

# int_lst = [10, 21, 4, 45, 66, 93] - option #2 to create own list of some digits 
  
# 1.1 Check list if it contains odd numbers - Using 'break' operator iterating each number in the list 
for num in int_lst: 
    # checking condition 
	if (num % 2) == 1: 
		print (num)
		# double condition allows 
	elif (num % 2) != 1:
		pass
	else:
		break # using break

# 1.2 Check list if it contains even numbers - Using 'break' operator

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

#OPTIONAL # 'odd number checking' is not necessary

# 1.3 Check list if it contains odd numbers - Using 'break' operator (Liybov Koliasa example)

#for i in range (1,10):
	#(list(str(i))) # дізнатись як створити

num_odd = False

for i in int_lst:
	if (i % 2) != 0:
		num_odd = True
		break
if num_odd:
	print ('There is an odd number here')
else:
	print ('There is only even numbers here')

#OPTIONAL # '1.3.3 odd number checking' is not necessary

