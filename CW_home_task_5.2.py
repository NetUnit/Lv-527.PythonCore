# codewars task2 'Will there be enough space?' - SoftServe5 - Lesson5

# 1.2 The number of passengers he can't take
# Bob is quite a lazy so his idea is counting of passengers not available to take a seat (instead of counting available seats in a bus)

def enough(cap, on, wait):

	# cap is the amount of people the bus can hold excluding the driver.	
	# on is the number of people on the bus.
	# wait is the number of people waiting to get on to the bus.
	
	occupied_seat_num = on + wait - cap

	if occupied_seat_num < 0:
		return 0 #estimated number of passengers impossible to take
	else:
		return occupied_seat_num

print ( enough (10, 5, 5) )


# 1.2 Function that tells you if it is enough space for passengers in a bus:

def enough(cap, on, wait):

	# Bob is a driver and he agrees to count people in the bus
	
	free_seat_num = cap - (on + wait)
	if free_seat_num > 0:
		return str(0) + ' people is unavailable to take into the bus'#estimated number of passengers impossible to take
	elif free_seat_num == 0:
		return 'The numbers of free seats is: ' + str(free_seat_num) + ' seats. We are sorry of that :('
	else:
		return 'The number of people unavailable to take: ' + str(abs(free_seat_num))  


cap = int(input ('Bob, please select the number of total seats in your bus: '))
on = int(input ('Bob, please select the current number of people in the bus: ')) # if it's hard to Bob to estimate people inside he might passengers to count themselves
wait = int(input ('Please select the number of people waiting now at a bus-stop: ')) 

print ( enough (cap, on, wait) )

# OPTIONAl # good example of that is cap = 40, wait = 25, on = 17. Perfect for Lviv.