# codewars task2 - SoftServe#4 - Lesson4

# You need to write a function that reverses the words in a given string. A word can also fit an empty string.

# OUR STRING IS: 'Word1 Word2'

#Exmaple1
def reverse(st):
    # Your Code Here

	return '{1}, {0}'.format ('Word1', 'Word2')

st1 = reverse('Word1 Word2') 
print (st1)
st2 = st1.replace(',', ' ')
print ( st2 )

# not relevant with 'code wars'

#Example2
def reverse(st):
	w = st.split() # split will create a list with separate objects into a 'list'. one 'object' is one word.
	w.reverse() # will reverse the order of objects | singular perfomance function
	#print (w)
	return " ".join(w)  # will return objects in the 'str' format with gaps | singular perfomance function

stri = "Hello World"

print(reverse(stri))

# relevant with 'code wars' # using 'split' method and list reversing

