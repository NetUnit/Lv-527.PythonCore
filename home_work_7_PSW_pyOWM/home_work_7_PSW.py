# homework_task 1'Passw0rd Complex'- SoftServe7 - Lesson7

import string
import re
import time

time.sleep(0.75)
print ('METHOD#1: ')
time.sleep(0.75)


#1.1.1 Validity of PSW. Using 're' MODULE and findall() method # without cycle

''' [a-z] and [A-Z] one letter from the list should be included \n\
    [0-9] one digit from the list should be included.\n\
    [$#@] one character from the list should be included.\n\
    Minimum length 6 characters.\n\
    Maxim m length 16 characters\n")
'''

psw = input ('PROVIDE A KEY: ')

# when feature_1 is step-by-step: code doesn't work
feature_1 = re.findall('|'.join(string.ascii_lowercase), psw)
feature_2 = re.findall('|'.join(string.ascii_uppercase), psw)
feature_3 = re.findall('|'.join( [ str(i) for i in range (0, 10) ] ), psw)
feature_4 = re.findall('|'.join('@#' ), psw) # DOLLAR SIGHN DOESNT WORK #will return empty brackets


if feature_1 and feature_2 and feature_3 and feature_4 and 5<len(psw)<17: 
	print ('YOUR PASSWORD IS VALID')
else:
	print ('YOUR PASSWORD IS INVALID')


#1.1.2 Validity of PSW. Using 'string' MODULE and any() method

time.sleep(0.75)
print ('METHOD#2: ')
time.sleep(0.75)

def psw_key(psw):

	''' This peace of code describes the cycle which will execute
	3 times and end-up when b reaches 0 value
	when wrong password 3 times - might put a clock for 10mins (600sec and repeat the cycle)
	time.sleep(600)
	'''
	b = 3
	while b > 0:
		b = b - 1
		
		if b == 0: #relates to formula # all after this attement will execute b-times according to a formula
	   		break

	   	psw_lst = list (psw)
		symbol_lst = list('$@#')
		
		result = any ([i.islower() for i in psw_lst]) and any([i.isupper() for i in psw_lst]) and any([i.isdigit() for i in psw_lst ]) and any([i in psw_lst for i in symbol_lst])

		#i.islower() - find Lowercase letter in the password #type 'boolean'
		#i.isdigit() - find digit in the password 
		#i.isupper() - find Uppercase letter in the password
		# compares symbol_lst with psw_lst (if symbols exists in in psw_lst)

		print (result)

########################### EXECUTION ############################## #### make it via function again

		if result and 6<=len(psw_lst)<= 16: # if result == True
			return ('CORRECT. ACCESS GRANTED')
			exit()

		elif result !=True or len(psw_lst)<6 or len(psw_lst)>16:
			psw = input ('ACCESS DENIED. PROVIDE A KEY: ')
			
		else:
			pass

		if b == 1: 

			psw_lst = list (psw)
			result = any([i.isdigit() for i in psw_lst ]) and any([i.isupper() for i in psw_lst]) and any ([i in psw_lst for i in symbol_lst])

			if result !=True or 6>len(psw_lst)>16 :
				return ('YOUR ACCOUNT HAS BEEN BLOCKED FOR 10 MINUTES')

			elif b == 1 and result and 6<=len(psw_lst)<= 16:
				return ('HUHHH!. ACCESS GRANTED')

			else: #relates to formula # all after this statetement will execute b-times according to a formula
	   			break
	
psw = list (input ('PROVIDE A KEY: ')) # will execute b-times (3) as in the cycle (including specific condition when b == 1)

print(psw_key(psw))


