
# codewars task3 - 'Double Char'- SoftServe8 - Lesson8

# #1.3.1 Given a string, you have to return a string in which each character (case-sensitive) is repeated once

# lambda
def double_char(s):
    lst = list (map(lambda x:x*2, s))
    lst2 = ''.join(lst)
    return (lst2)

#RELEWANT WITH CODEWARS

# #1.3.2 LC
#Example2
def double_char(number):
	
	return ''.join([x*2 for x in s])

#RELEWANT WITH CODEWARS

# 1.3.3 enumerate
#Example3

def double_char(s):
	
	my_lst = list (map(str, s))
	for (index, elem) in enumerate(my_lst):
		my_lst[index] = elem*2


#1.3.4 using for cycle
#Example4
def double_char(s):
	element = []
	for i in s:
		element=element+[i]*2

	element = ''.join(element)
	return element

s = input ('Please type your list: ')
print (double_char(s))
