# codewars task5 'Сounting sheep'- SoftServe5 - Lesson5 


#1.1 Function that counts the number of sheep present in the array (true means present)

def count_sheeps(sheep):
	if True and False in sheep:
		x = sheep.count(True)
		y = sheep.count(False)
		return str(x) + ', There are ' + str(x) + ' sheeps in total, not ' + str(y)
	else:
		pass
sheep = [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1] # own list of numbers

print (count_sheeps(sheep))

# NON-RELEVANT WITH CODEWARS

#1.2 a Function that counts the number of sheep present in the array (true means present)

array1 = [True,  True,  True,  False,
		  True,  True,  True,  True, 
		  True,  False, True,  False,
		  True,  False, False, True,
		  True,  True,  True,  True,
		  False, False, True,  True ]; 

def count_sheeps(sheep):
  # TODO May the force be with you
		return str(sheep.count(True)) + ' sheeps in total, not %s%d' % ('present ', sheep.count(False))
print (count_sheeps (array1))

# NON-RELEVANT WITH CODEWARS

#1.3 Using a method count() 
def count_sheeps(sheep):
    return sheep.count(True)
print (count_sheeps(array1))

# RELEVANT WITH CODEWARS

#1.4 Using the 'LC'
def count_sheeps(sheep):
		lst = [str(i) for i in sheep if i == True  ] # or [str(i) for i in sheep if i ]
		# print (type(lst)) # class list
		return len(lst)
print (count_sheeps(array1))

# RELEVANT WITH CODEWARS

# https://www.codewars.com/kata/54edbc7200b811e956000556/solutions






