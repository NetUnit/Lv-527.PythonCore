
# codewars task2 - 'Reverse List Order'- SoftServe7 - Lesson7

#1.2.1 In this kata you will create a function that takes-in a list and returns a list with the reverse order.

def reverse_list(l):
    lambda_lst = list(map(lambda x: x, l)) # using lambda function
    lambda_lst.reverse()
    return lambda_lst

l = input ('Enter some parts of your list: ') 
print (reverse_list(l))

#RELEWANT WITH CODEWARS

#1.2.2
#Example2
def reverse_list(l):
    return [i for i in l ][::-1] # using list slice

l = input ('Enter some parts of your list: ') 
print (reverse_list(l))																															

#RELEWANT WITH CODEWARS
