
# codewars task1 - 'Grasshopper - Summation'- SoftServe8 - Lesson8

#1.2 lambda expression

def summation(number):
	if number > 0:
		return sum(list(filter(lambda x: x+x, [i for i in range (1, number+1)])))
	else:
		pass
		
number = int(input ('Enter a number: '))
print (summation(number))


#1.2 map
def summation(num):

	return sum (list ( map (int, range(1, num+1) ) ) )

num = int(input ('Enter some number: '))
print (summation(num))

#1.3 cycle for

def summation(num):
	
	b=[]
	for i in range(0, num+1):
  		b=b+[i] # наповнення списку елементами заданими в циклі

	return sum(b)

num = int(input ('Enter some number: '))
print (summation(num))


