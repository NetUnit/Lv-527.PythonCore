# codewars task2 '21 sticks'- SoftServe6 - Lesson6
import random
import time

#2.1 Create a robot that will always win the game. Your robot will always go first. The function should take an integer and returns 1, 2, or 3.

def make_move (sticks):

	x = int(sticks)

	# robot wil be y
	# human will be z

	y = random.randint(1, 3)
	z = random.randint(1, 3)

	while x >= 0:
		x = x - y - z 

		time.sleep(0.5)
		
		print(y, ' Robot')
		print (z, ' Human')
		print (x, ' = Residue')

		if x == 5:
			y = 1

		elif x == 3:
			y = 3
			return ('The next Y will be - 3. Y has won as usual.')

		elif x == 2:
			y = 2
			return ('The next Y will be - 2, Y has won as usual')

		elif x == 1:
			y = 1
			return ('The next Y will be - 1, Y has won as usual')

		if x == 0:
			print ('Congrats, Y has won as usual')
			break

sticks = input ('Please select the quantity of sticks: ....should be 21...: ')
print (make_move (sticks))

# NON-RELEVANT WITH CODEWARS # 








