import string
import re
# codewars task3 - 'Remove the time'- SoftServe9 - Lesson9

# 1.1 Assume shortenToDate's input will always be a string, e.g. "Friday May 2, 7pm". Assume shortenToDate's output will be the shortened string, e.g., "Friday May 2".

# using re.sub() + spli() + join
import re

def shorten_to_date(long_date): 
    result = (re.sub(r'[,\s]',' ', long_date)).split()   #'[,\s]' - pattern, will delete all commas in the string. ' ' - part between words (aplly to all spaces between words)
    return ' '.join(result[:-1])

#1.2 using replace() method + list slice + join

def shorten_to_date(long_date):
    long_date = long_date.replace(',', '') 
    result = ' '.join((long_date.split())[:-1]) 
    return result

#print (shorten_to_date("Monday February 2, 8pm"))
#print(shorten_to_date("Tuesday May 29, 8pm"))
#print(shorten_to_date("Wed September 1, 3am"))
#print(shorten_to_date("Friday May 2, 9am"))
#print(shorten_to_date("Tuesday January 29, 10pm"))




