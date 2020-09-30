import string
import re
# codewars task1 - 'Is the string uppercase?'- SoftServe9 - Lesson9

# 1.1 In this Kata, a string is said to be in ALL CAPS whenever it does not contain any lowercase letter so any string containing no letters at all is trivially considered to be in ALL CAPS.

# using any
def is_uppercase(inp):

	character_lst = (list(string.ascii_letters.lower()))

	result =  any(i in inp for i in (character_lst)) # any return bool data - True/False
	if not result:
		return True
	else:
		return False

inp = input ('Type a text U want to check-out: ')

print (is_uppercase(inp))

#1.2 using islower() method (positive condition)

def is_uppercase(inp):
    if any ([i.islower() for i in inp]) != 0: # returns True/False when lowercase exist/not exist in the list
        return False
    else:
        return True
#1.3 (negative condition)
def is_uppercase(inp): 
    if any ([i.islower() for i in inp]) == 0: # returns True/False when lowercase exist/not exist in the list
        return True
    else:
        return False

#1.4 using lambda ex
def is_uppercase(inp):
	lst_inp = list ( map (lambda x: x, inp))
	lst_match = list(string.ascii_lowercase) # requires a 'string' module as necessary

	for i in lst_inp:
		if not i in lst_match:
			return True
		else:
			return False

inp = input ('Please type some text: ')
print (is_uppercase(inp))

