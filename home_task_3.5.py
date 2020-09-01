import time
# task5 - SoftServe#4 - Lesson4

#1.1 Create the list of Fibonacci Numbers using cycle (while, for) up to 13

# Fn = Fn-1 + Fn-2
# F0 = 0, F1 = 1

# Function to create Fibonacci number using condition

n = int(input ('Type the Fibonacci number:')) 

def Fibonacci(n): 
    if n<0: 
        print("Incorrect input") 
    # First Fibonacci number is 0 
    elif n == 1: 
        return 0
    # Second Fibonacci number is 1 
    elif n == 2: 
        return 1
    # The third Fibonacci number is 1
    else: 
        return Fibonacci(n-2)+Fibonacci(n-1) 

print(Fibonacci(n)) 

#1.2 Create the list of Fibonacci Numbers using not efficient recursive function + cycle for - https://stackoverflow.com/questions/494594/how-to-write-the-fibonacci-sequence

time.sleep(2)

r = int(input ('Type the Fibonacci range:'))

def rec_fib(n): # recursion function 
    '''inefficient recursive function as defined, returns Fibonacci number - works only up to 30''' 
    if n > 1:
        return rec_fib(n-1) + rec_fib(n-2) # described the formula Fn = Fn-1 + Fn-2 through function
    return n

for i in range(r):
    print(rec_fib(i))

time.sleep(2)

#1.3 Create the list of Fibonacci Numbers using cycle (while) - https://www.programiz.com/python-programming/examples/fibonacci-sequence

# Program to display the Fibonacci sequence up to n-th term

nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto", nterms, ":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1


#WRONG
#n = int(input ('Type the Fibonacci number:')) 

#def Fibonacci(n):
	#a, b = 1, 1
	#a, b = b, a + b
	#while True:
  		#return Fibonacci(n-2)+Fibonacci(n-1)
  		#if n<0: 
    		#print("Incorrect input")

#print(Fibonacci(n))




#WRONG
#n = int(input ('Type the Fibonacci number:')) 

#def Fibonacci(n): 
    #for i in range(n):
        #return(Fibonacci(n-2)+Fibonacci(n-1))
  
#print(Fibonacci(n))


# WRONG
#num1 = int(input ('Type the first number:'))
#num2 = int(input ('Type the second number:'))
#num3 = int(input ('Type the Fibonacci number:'))

#def Fibonacci(num3):
	#for i in range (num1, num2):
		#print(num3)

		#if num3 <0:
			#print ("Incorrect input") 
		#elif num3 == 1:
			#return 0
		#elif num3 == 2:
			#return 
		#else:
			#return Fibonacci(num3-1)+Fibonacci(num3-2)
	
#Fibonacci(num3)


