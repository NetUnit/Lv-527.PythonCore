# codewars task1 'Will you make it?' - SoftServe5 - Lesson5

# Function that identifies you if it is possible to get to the pump or not.

def zero_fuel(distance_to_pump, mpg, fuel_left):
    #Happy Coding! ;)
   
    coverage = (mpg)/((distance_to_pump/fuel_left)) #coverage is the value that describes our function (dependancy bettwen distance and fuel amount)
    
    if coverage >= 1:
    	return True
    else:
    	return False

distance_to_pump = int(input ('Please select the distance to a pump: '))
fuel_left = int(input ('Please select the amount of fuel in the tank: ')) 
mpg = int(input ('Please select the mpg rate of your car: ')) # mpg - miles per gallon (1 litr of fuel - 25miles)

print (zero_fuel(distance_to_pump, mpg, fuel_left))

