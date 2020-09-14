# codewars task3 'Are U Playing Banjo?'- SoftServe5 - Lesson5 

#1.1 Function that asks U whether U play banjo:

def areYouPlayingBanjo(name):
    # Implement me!
    
 	#2 using the list comprehension lst = [str(i) for i in str(name)]

 	lst = list(name) #1 method: list function()
 	#print (type(lst)) # we've crated a list from a single word to iterate it through 'R' and 'r'

 	if 'R' in lst[0] or 'r' in lst[0]: 
 		return name + ' plays banjo'
 	else:
 		return name +  ' does not play banjo'

name = input ('Please enter the name of a banjo-player: ')

print (areYouPlayingBanjo( name ))

#1.2 Function that asks U whether U play banjo:

def areYouPlayingBanjo(name):
	lst = [str(x) for x in str(name)]
	if "R" in lst[0]:
		return name + " plays banjo"
	elif 'r' in lst[0]:
		return name + " plays banjo"
	else:
		return name + ' does not play banjo'

print(areYouPlayingBanjo(name))