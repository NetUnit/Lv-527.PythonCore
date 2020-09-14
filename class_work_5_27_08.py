import sys
import time

#classwork2 27.08 - SoftServe#5 - Lesson5

# 5.1 Create the list of integers, determine 'max' and 'min'

num = input ('Type some number: ')
int_lst = [int(x) for x in str(num)] # creating the list of integers using 'LC'
print (int_lst) # creating the list

print ('The maximum number in the list is: ', max(int_lst))
print ('The minimum number in the list is: ', min(int_lst))


#5.2 In the range from 1-10 determine even numbers, odd numbers which divides to 3 (apart - 1), numbers which not divides to 2 or 3 
# USING 'LC'

def number(num):

	even_lst = [ str(i) for i in range (1, num) if i%2 == 0 ]
	odd_lst = [ str(i) for i in range (1, num) if i%2 == 1 ]
	non_div = [ str(i) for i in range (1, num) if i%3 != 0 and i%2 != 0  ]

	even_lst.insert (0, 'This is the list of evens:')
	odd_lst.insert (0, '. This is the list od odds:')
	non_div.insert (0, '. This is the list of 2∕3 not divisible:')

	total = even_lst + odd_lst + non_div
	total2 = ' '.join(total)

	return total2

num = int(input ('Please type the last digit in your range: ')) + 1 # our latter digit in the range should be 11

print (number(num))

#5.3.1 Function (program that counts factorial) 

def factor(n):
	i = 1 # assign our variable before condition, otherwise 'UnboundLocalError: local variable 'i' referenced before assignment'
	while n > 1:
		i = i * n
		n = n - 1
	return i

n = int(input ('Type the factorial number U want to count:')) 
print(factor(n))

#5.3.2 Using 'for' cycle (program that counts factorial)
#Example2

def factor2(n):
	factorial = 1
	for i in range (1, n+1):
		factorial = factorial * i
		#n = n -1
	return (' The factorial of {0} is {1}'.format(n, factorial)) # форматування виведеного тексту

n = int(input ('Type the factorial number U want to count:'))

print (factor2(n) )

#5.3.3 Function (program that counts factorial)
#Example3

#def factor(n):
	#i = 1
	#while n >= 0:
	   #i = n * ( n - 1 )
	#return i

#n = int(input ('Type the factorial number U want to count:')) 
#print(factor(n))

# DOESN'T WORK

#5.4.1 Login/Password

def psw_key(psw):

	psw_list = ['First!']

	b = 3
	while b > 0:
		b = b - 1
		
		if b == 0: #relates to formula # all after this attement will execute b-times according to a formula
	   		break

		# EXECUTION ########################################################################################

		if psw in psw_list: # relates to a key
			return ('CORRECT. ACCESS GRANTED')
			exit()

		if not psw in psw_list: # relates to a key
			psw = input ('ACCESS DENIED. PROVIDE A KEY: ')
			
			if b == 1 and psw != 'First!':
				return ('YOUR ACCOUNT HAS BEEN BLOCKED FOR 10 MINUTES')
			if b == 1 and psw == 'First!':
				return ('HUHHH!. ACCESS GRANTED')

psw = input ('PROVIDE A KEY: ') # will execute b-times (3) as in the cycle (including specific condition when b == 1)

print(psw_key(psw))

# 3 ATTEMPTS TO SIGHN-IN - Login/Password using 'while' cycle


#5.4.2 Login/Password
#Example2

password = input ('PLEASE ENTER A PASSWORD:')

if password == 'User123':
	print('Correct. Access granted')
	exit()

def check_psw():
	time.sleep(2)
	print('Correct. Access granted')

trial2 = input ('PLEASE SELECT A PROPER PASSWORD:')
if trial2 == 'User123':
	check_psw() # 2nd trial check
if not trial2 == 'User123':
	trial3 = input ('PLEASE SELECT A PROPER PASSWORD:')	
	
	if trial3 == 'User123':
		check_psw() # 3rd trial check

	if not trial3 == 'User123':
		time.sleep(2)
		print ('YOU HAVE NOT CHOSEN A CORRECT ANSWER. PLEASE TRY AGAIN IN 10 MINUTES')
		pass

# 3 ATTEMPTS TO SIGHN-IN - Login/Password using while cycle
#### UGLY VERSION - NON-RELEVANT WITH 'PYTHON-ZEN'


#5.4.3 # 3 ATTEMPTS TO SIGHN-IN - Login/Password using while cycle 
#Example3

def sighn_in(psw):

	if psw == 'User123':
		print ('Correct. Access granted')
		exit()
	
	b = 2 # function will execute 2 times more
	while psw != 'User123':
		b = b - 1

		psw = input ('Acces Denied. Please enter the password:') #1st step
		
		##############################################################################################
		
		if psw == 'User123': #2nd condition
			print ('Access granted')
			exit()

		elif b == 1: #2nd condition2
			psw = input ('Acces Denied. This your last attempt. Please provide a correct password:')

		################################################################################################
			if psw == 'User123':
				print ('Access granted')
				exit()

			else:
				print ('Soryy U haven\'t provided a correct answer.') #3rd condition 3d step
				exit()

psw = input ('Please enter the password:') #1st step
print(sighn_in(psw))

# 3 ATTEMPTS TO SIGHN-IN - Login/Password using while cycle


