# codewars task4 'Unfinished Loop - Bug Fixing #1'- SoftServe6 - Lesson6

#4.1 Oh no, Timmy's created an infinite loop! Help Timmy find and fix the bug in his unfinished for loop!

def create_array(n):
    res=[]
    i=1
    while i<=n:
        res = res + i
        i = i + 1

        if i == n+1:
            break
    return res

# RELEVANT WITH CODEWARS - http://joxi.net/DmBb187T45JdKm

def create_array(n):
	i=1
	while i<=n:
		print (i)
		i = (i + 1)   	
		
		if i == n+1: #without + 1 - utmost i = (i-1)
			break

n = int(input ('Number: '))
create_array(n)

# check-out cycle



	










