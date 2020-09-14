# codewars task4 'Boolean'- SoftServe5 - Lesson5 


#1.1 Convert boolean values to strings 'Yes' or 'No':

def bool_to_word(boolean):

	a = 75
	b = boolean

	if a > 0 and b > 0: #using double condition
		return 'Yes'
	else:
		return 'No'

print (bool_to_word(-25))
# only one relevant with codewarsdef bool_to_word(boolean):

#1.2
def bool_to_word(boolean):
    c = 30
    t = c % boolean
    if t == 0:    
        return ('Yes')
    else:
        return ('No')

print(bool_to_word(6))
# NOT RELEVANT WITH CODEWARS

#1.3
def bool_to_word(boolean):

    if 30 % boolean == 0:  
        return ('Yes')
    else:
        return ('No')

print(bool_to_word(7))
# NOT RELEVANT WITH CODEWARS

#1.4
def bool_to_word(boolean):
	lst = [1 , 2 , 3, 4, 5, 6, 7, 8, 9, 10]
	for x in lst:
		if x%boolean == 0:
			return 'Yes'
		else:
			return 'No'

print (bool_to_word(2))
# NOT RELEVANT WITH CODEWARS

#1.5
def bool_to_word(boolean):
	x = 73
	if x%boolean == 0:
		return 'Yes'
	else:
		return 'No'

print (bool_to_word(1))
# NOT RELEVANT WITH CODEWARS

