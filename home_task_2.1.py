# task1 - SoftServe#3 - Lesson3
# Use string to depict the Zen of Python (Python philosophy)

zen_python = '''

The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''

#task 1.1 "Find and count in the text above number of words (better, never, is)" - (in order to implement this - use 3 separate variables, not single)

count_better = zen_python.count ('better')

count_never = zen_python.count ('never')

count_is = zen_python.count ('is')

# count will return 'int' - need to convert to 'str' then

print ( 'This text contains the next quantity of words \'better\' - ' + str(count_better) + ' words, \'never\' - ' + str(count_never) + ' words, \'is\' - ' + str(count_is) + ' words' )

#task 1.2 - "Print text given above in the Uppercase format (all uppercase letters)" 

upper_zen = zen_python.upper ()

print ( upper_zen )

#task 1.2.1 (as an option we will sum the quantity of all letters in the text, except other symbols). https://www.cyberforum.ru/python-beginners/thread2226706.html #OPTIONAL 

def extra_count ():
	symbols = len ( zen_python ) - zen_python.count (' ') - zen_python.count ('.') - zen_python.count ('!') - zen_python.count (',') # number of symbols (letters) 
	words = zen_python.count (' ') + 1 # number of words

	print ( 'The following text contains the next number of letters - ' + str (symbols) + ' and ' + str  ( words ) + ' words' ) 
extra_count()

#OPTIONAL # 'extra_count ()' is not necessary

# 1.3.1 shift symbols 'i' and '!' with '&' and '_'

shift_symbols = zen_python.replace('i', '&')
print ( shift_symbols )

#1.3.2 another option of doing this:      
count_i = zen_python.count ('i') # will counting the number of 'i' symbols (as in the instruction - https://www.programiz.com/python-programming/methods/string/replace )
shift_symbols_optional = zen_python.replace('i', '&', count_i ) # using the counted number as a number of shifts 'i' to '&' 
print ( shift_symbols_optional )

#OPTIONAL # 'count_i' is not necessary





