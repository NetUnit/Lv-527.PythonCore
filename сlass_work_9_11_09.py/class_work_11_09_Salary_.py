import numpy as np
from math import sqrt
import copy
import time

# classwork1 'class Salary' - SoftServe#9 - Lesson9 OOP


'''

'''

# using % operator to represent data


class Name:

    name = 'John'
    lastname = 'Smith'
    balance = 4500

    def __init__(self, name=name, lastname=lastname, balance=balance):
        self.name = name
        self.lastname = lastname
        self.balance = balance

    def balance_for_person(self, name, lastname, balance):
        return 'Місячна зарплата для %s %s, складає %d usd' % (name, lastname, balance)
    # return f'Місячна зарплата для {name} {lastname}, складає {balance} usd' - еквівалент


# parameter by default when
# not being setup here
name_selection = Name()
print(name_selection.balance_for_person('Kim', 'Nolo', 6000))


# протіерувати кожен елемент dict щоб надати йому str значення
print('%(language)s has %(number)03d quote types.' %
      {"language": "Python", "number": 2})


def formatting(par):
    features = par.split()
    # ключі повертаються в int форматі треба надати їм str
    features = dict(enumerate(features))
    # return features

    return 'Місячна зарплата для %(0)s has %(1)s' % dict(enumerate(features))


par = input(
    'Please select the next items through space: NAME, LASTNAME, SALARY: ')
print(formatting(par))
