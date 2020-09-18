
# codewars task1 - 'Count of positives / sum of negatives'- SoftServe7 - Lesson7

#1.1 Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers

def count_positives_sum_negatives(arr):

	if len(arr)!=0:
		pos = len([int(x) for x in arr if int(x)>0])
		neg = sum([int(x) for x in arr if int(x)<0])
		return [pos, neg]
	else:
		return []

#RELEVANT WITH CODEWARS 

#Example 2 Try Lambda

def count_positives_sum_negatives(arr):
	if len(arr) != 0:
		pos = len(list(filter(lambda x: x > 0, arr))) 
		neg = sum(list(filter(lambda x: x < 0, arr)))
		return [pos, neg]
	if len(arr) == 0:
		return []

print(count_positives_sum_negatives(arr))

#RELEVANT WITH CODEWARS

