# codewars task3 - SoftServe4 - Lesson4 

#3.1.1 Using different ways to format strings

partner_sel = input('Type your name: ')

def greet(name):
    if name == "Johny":
        return "Hello, my love!"
    else:
        return "Hello, {name}!".format(name=name)

print(greet(partner_sel))
# RELEVANT WITH CODEWARS

#3.1.2
partner_sel = input('Type your name: ')

def greet(name):
	if name != 'Johny':
		return ("Hello, {}!".format(name)) # the second method of doing this
	else:
		return ("Hello, {name}!".format(name = 'my love'))

print(greet(partner_sel))
# the simplest option (NON-RELEVANT WITH CODEWARS)


partner_sel = input('Type your name: ')

def greet(name):
	if name != 'Johny':
		return ("Hello, {name}!".format(name = name)) # variable in brackets/variable=variable
	else:
		return ("Hello, {name}!".format(name = 'my love')) # variable in brackets/variable=variable

print(greet(partner_sel))
# (NON-RELEVANT WITH CODEWARS)


partner_sel = input('Type your name: ')

def greet(name):
	if name == 'Johny':
		return ('Hello, {name}!'.format(name = 'my love')) # the second method 
	else:
		return ('Hello, {name}!'.format(name=name))

print(greet(partner_sel))
# (NON-RELEVANT WITH CODEWARS) - https://prnt.sc/ubrbnp


partner_sel = input('Type your name: ')

def greet(name):
	if name != 'Johny':
		return (f'Hello, {name}!') # the second method of doing this
	else:
		return ('Hello, my love!')

print(greet(partner_sel))
# (NON-RELEVANT WITH CODEWARS) - https://prnt.sc/ubr9ae


partner_sel = input('Type your name: ')

def greet(name): 
	return "Hello, {}!".format(name.replace("Johnny", "my love")) # replace will only execute when name = 'Johny'∕if not - pass
print(greet(partner_sel))

##1 SIMPLEST∕RELEVANT WITH CODEWARS


