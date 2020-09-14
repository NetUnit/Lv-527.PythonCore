#task2 - SoftServe#3 - Lesson3

#CREATE A POSITIVE 4-DIGIT INTEGER NUMBER

#2.1 Commit the multiplication of digits of this number:

int_lst = 1234
int_lst2 = str (int_lst ) # 1234 - but in string format  # need to convert to 'str' firstly, othercase "TypeError: 'int' object is not iterable"
str_lst = [str(x) for x in int_lst2] # ['1', '2', '3', '4'] # int object - not str

# print  ( str_lst )

print ( str (str_lst) + ' - We have created a list from random digits' )

multipl = int(str_lst[0]) * int(str_lst[1]) * int(str_lst[2]) * int(str_lst[3])
print ('Multiplication result: ' + str (multipl) )

#2.2.1 print this number in the reverse order
# using regular indexes

print ( int_lst2[3] + int_lst2[2] + int_lst2[1] + int_lst2[0] )


# 2.2.2 using minus indexes 
# Example#2

print ( int_lst2[-1] + int_lst2[-2] + int_lst2[-3] + int_lst2[-4] )


# 2.2.3 using reverse method
# Example3

reversed_lst = str_lst.reverse() # optional 3

def convert(str_lst): ### IMPORTANT CONVERTING LIST [] TO TUPLE FORMAT ()
    return tuple( str_lst )

converted_lst = convert ( str_lst ) # from LIST to TUPLE

strings = [str(integer) for integer in converted_lst] ### converting from string TUPLE∕LIST∕CORTEGE∕DICTIONARY
a_string = "".join(strings)
an_integer = int(a_string)

print ( an_integer  )


# 2.2.4 The format() method that is available with the string
# Example4

#reverse_order = "{2}, {1}, {0}, {0} ".format( str_lst ) # doesnt work - INDEX ERROR
#print ( reverse_order )
# DOESN'T WORK


# 2.3 Sort-out the digits which includes this number

print (dir(str_lst)) # identified that the source-method exists # The dir() method tries to return a list of valid attributes of the object

# 2.3.1 Method #1 : Using list comprehension - https://www.geeksforgeeks.org/python-convert-number-to-list-of-integers/
# creating a random natural number 
num = 1234

# printing number  
print ("The original number is: " + str(num))

# using list comprehension to convert number to list of integers 

int_lst = [int(x) for x in str(num)] #we will get the list of integers
# without list comprhension

# printing result  
print ("The list from number is: " + str(int_lst)) 

reversed_lst = int_lst.reverse() # reversing int_lst - WILL RETURN None

print ("The reversed list is: " + str(int_lst))

# using 'sort' method to sort digits

sorted_lst = int_lst.sort() # sort the list in ascending order - WILL RETURN None

print ("The sorted list is: " + str(int_lst))

# 2.3.2 Method #2 : Using map() - https://www.geeksforgeeks.org/python-convert-number-to-list-of-integers/
# Example2

int_lst = list(map(int, str(num))) # to convert number to list of integers
reverse_lst = int_lst.reverse() 
print (int_lst ) # printing reversed list of integers
sort_lst = int_lst.sort() # sorting - https://stackoverflow.com/questions/1301156/how-to-sort-digits-in-a-number
print (int_lst) # printing the list of integers put in the logic order


# 2.3.3 Method #3 : Sort the digits in ascending and descending orders - https://stackoverflow.com/questions/1301156/how-to-sort-digits-in-a-number
# Example3

num = 2020 # creating a random number
ascending = "".join(sorted(str(num)))
print ( ascending )





