# classwork10 - SoftServe#10 - Lesson10


'''
	1.1 Write a program that prompts the user to enter an integer and
	determines whether the number is even or odd, taking into account
	the case of entering incorrect data.
'''


def check(x):

    if x % 2 == 0:
        return ('This is an even number')

    if not x % 2 == 0:
        return ('This is an odd number')


x = float(input('Please type your value: '))

try:
    print(check(x))

except ValueError as err:
    print(f'This is a ValueError - {(err)}')

except TypeError as err:
    print(f'This is a TypeError - {(err)}')

except ZeroDivisionError as err:
    print(f'This is a ZeroDivisionError - {(err)}')


'''
	Write a program that prompts the user to enter their age,
	and then displays a message stating whether the age is
	even or odd. The program must provide the ability to enter
	a negative number, and in this case generate an exception.
	The master code should call a function that processes the
	information entered. 

	Switched separately when user is typing the negative
	Value - raising the error and catch it.
'''


class Age:

    def __init__(self, age=0):
        self.age = age

    def set_age(self, age):
        try:
            if age % 2 != 0 and age >= 0:
                return f'Your age-number is even: {age}'
            elif age % 2 != 1 and age >= 0:
                return f'Your age-number is odd: {age}'
            else:
                raise TypeError('Ooops. Bad input')
        except TypeError as err:
            return f'Please provide correct data, error: {err} was caught'
        except ValueError as err:
            return f'Please provide correct data, error: {err} was caught'


instance = Age()
print(instance.set_age(int(input('Please select your age: '))))


'''
	1.3 Write a program to calculate the divide of two
	numbers entered by the user sequentially through a comma,
	to predict the case of division by zero, cases of syntactic
	errors and cases of other exceptional situations. Use the
	else and finally blocks
'''


def check(x, y):

    try:
        return int(x)/int(y)

    except ValueError as e:
        return ('This is a ValueError', e)

    except TypeError as e:
        return ('This is a TypeError', e)

    except ZeroDivisionError as e:
        return ('This is error a ZeroDivisionError - ', e)

    finally:
        print('All errors r being caught')


x = input('Please type your value: ')
y = input('Please type your 2nd value: ')

print(check(x, y))


'''	
	1.4 Write a program that analyzes the entered number and,
	depending on the number, gives the day of the week 
	that corresponds to this number (1 is Monday, 2 is Tuesday, etc.).
	Take into account cases of entering numbers from 8 and more, 
	as well as cases of entering non-numerical data
'''


class Weekday:

    weekdays = ['Monday', 'Tuesday', 'Wednesday',
                'Thursday', 'Friday', 'Saturday',
                            'Sunday']

    def disp_day(self, inquiry, weekdays=weekdays):
        try:
            inquiry = int(inquiry)
            return dict(enumerate(weekdays)).get(inquiry-1) if 0 < inquiry < 8 else 'Please provide a correct weekday'
        except:
            'Please select the relevant data'


selection = Weekday()
print(selection.disp_day(input('Please select the weekday: ')))
