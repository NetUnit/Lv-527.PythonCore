
# codewars task3 - 'Multiples of 3 or 5'- SoftServe7 - Lesson7

#1.3 If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

def solution(number):
	if number:
		return sum(list(filter(lambda x: x%3==0 or x%5==0, [i for i in range (1, number)])))
	else:
		return False
		
#RELEWANT WITH CODEWARS
