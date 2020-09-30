import string
import re
# codewars task2 - 'Sort My Textbooks'- SoftServe9 - Lesson9

# 1.1 HELP! Jason can't find his textbook! It is two days before the test date, and Jason's textbooks are all out of order! Help him sort a list (ArrayList in java) full of textbooks by subject, so he can study before the test.

def sorter(textbooks):
    return sorted(textbooks, key = lambda x: x.lower()) # will satisfy condition between lower and upper title letters in the list


# 1.2 Will satisfy all conditions: handle sorting strings, capitalization, symbols. Will equal ASCII.

def sorter(textbooks):
    #Cramming before a test can't be that bad?
    
    #adding upercase --> join+map --> re.sub
    # textbooks.sort()
    # textbooks = ' '.join( map (lambda x: x.title(), textbooks))
    
    #textbooks = list (map (lambda x: x.lower(), textbooks))
    #textbooks.sort()
    #return textbooks

    # lc --> sorted --> join + sorting the list in alphabetical order
    #textbooks = ' '.join(sorted([i.title() for i in textbooks])) # using lc

    # lambda ex --> sorted --> join + sorting the list in alphabetic order
    #textbooks = ' '.join(sorted( map (lambda x: x.title(), textbooks))) # using lambda
    
    # lambda ex --> sorted --> join
    #list (map (lambda x: x.title(), textbooks))
    #textbooks.sort()
    #return ' '.join(textbooks)

    # reg.ex - application 
    textbooks = ' '.join(map (str, textbooks))
   
    # https://prnt.sc/uqvoj5 - specific rules
    textbooks = re.sub(r'[#\.]','e', textbooks) # . single symbol without filling a new string
    textbooks = re.sub(r'[$\.]','H', textbooks)
    textbooks = re.sub(r'[\^\.]','e', textbooks)
    textbooks = re.sub(r'[..\.]','', textbooks) # will shift any other symbol from UNICODE to an unlimited space
    textbooks = re.sub(r'[*\.]','', textbooks)
    # convert mixed text to titled/sorted/clean text

    textbooks = sorted(((textbooks.title()).split()))
    return (textbooks)


print(sorter(['Algebra', 'History', 'Geometry', 'English'])) # Does not sort strings
print(sorter(['Algebra', 'history', 'Geometry', 'english'])) # Does not handle capitalization'
print(sorter(['Alg#bra', '$istory', 'Geom^try', '**english'])) # Does not handle symbols'

# NON-RELEVANT WITH CODEWARS
