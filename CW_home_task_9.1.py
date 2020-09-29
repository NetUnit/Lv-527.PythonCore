import string

# codewars task1 - 'Is the string uppercase?'- SoftServe9 - Lesson9

# #1.1 In this Kata, a string is said to be in ALL CAPS whenever it does not contain any lowercase letter so any string containing no letters at all is trivially considered to be in ALL CAPS.

# using 'any'
def is_uppercase(inp):

	character_lst = (list(string.ascii_letters.lower())) #will create a list of lowercase letters

	result =  any(i in inp for i in (character_lst)) 	 # check any similar lowercase in 'inp' to lowercase characters in alphabet list ('character list') 
	if not result:									 	 # using incorrect condition
		return True
	else:
		return False

inp = input ('Type a text U want to check-out: ')
print (is_uppercase(inp))
