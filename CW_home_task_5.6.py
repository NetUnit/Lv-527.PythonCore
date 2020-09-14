# codewars task6 - 'Is this my tail'- SoftServe5 - Lesson5 


#1.1 Correct the broken function to make sure that the second argument (tail), is the same as the last letter of the first argument (body) - otherwise the tail wouldn't fit!

def correct_tail(body,tail):
	
	#block1: let's try to convert an appropriate body part. As our equality depends on the last letter of body, which simoultaneosly = the first part of tail. 

	body_end = [ str(i) for i in str(body)] [-1] # first element selection
	tail_beg = [ str(i) for i in str(tail)] [0]  # last element selection

	if body_end == tail_beg or body_end == tail_beg.upper() or body_end.upper() == tail_beg:
		return True
	else:
		return False

	#print (type(body_end))
	#print (type(tail_beg))

body = input ('Please select the body of the animal: ')
tail = input ('Please select the tail of the animal: ')

print (correct_tail(body, tail))

# RELEVANT WITH CODEWARS

#1.1

def correct_tail(body,tail):

	# DO THE SAME IN SIMPLER WAY INDEXING STRINGS
	b = body [-1] # first element selection
	t = tail [0]  # last element selection

	if b == t or b == t.upper() or b.upper() == t:
		return True
	else:
		return False

correct_tail(body, tail)

# RELEVANT WITH CODEWARS





