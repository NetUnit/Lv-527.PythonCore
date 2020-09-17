# codewars task3 'No yelling!'- SoftServe6 - Lesson6

#3.1 Write a function taking in a string like WOW this is REALLY amazing and returning Wow this is really amazing.
# String should be capitalized and properly spaced. Using re and string is not allowed.

def filter_words(st):
	st2 = st[0] + st.lower()[1:len(st)] # or [1:]
	return ' '.join((st2.capitalize()).split())
#RELEVANT WITH CODEWARS


#Example2
def filter_words(st):
	st2 = st.lower()
	st3 = st2.replace( st2.lower(), st2.capitalize() ) 
	return ' '.join(st3.split())
#RELEVANT WITH CODEWARS


#Example3
def filter_words(st):
    a = ' '.join(st[0].capitalize().split())
    b = ' '.join((st.lower()[1:len(st)]).split())
    c = a + b
    return c
#RELEVANT WITH CODEWARS


#Example4
def filter_words(st):
        return " ".join((st.lower()).split()).capitalize()       
#RELEVANT WITH CODEWARS

## or

def filter_words(st):
    st1 = st.lower()
    return " ".join(st1.split()).capitalize()


#Example6
def filter_words(st):
    st1=st[0].capitalize()+st[1:].lower()
    return " ".join(st1.split())

st = input ('Type your Text: ')
print(filter_words(st))
#RELEVANT WITH CODEWARS



# In Python, the capitalize() method converts the first character of a string to capital (uppercase) letter.
# If the string has its first character as capital, then it returns the original string.

#insert(st[0], 0) - doesn't work with 'str' - only 'list'
#return st2.insert(st[0], 0) doesn't work with 'str' - only 'list'

