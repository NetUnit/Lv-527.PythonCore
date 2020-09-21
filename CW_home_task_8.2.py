
# codewars task2 - 'Fix the loop!'- SoftServe8 - Lesson8

#1.2.1 Ваш колега написав простий цикл, щоб перерахувати своїх улюблених тварин. Але в граматиці, здається, є незначна помилка, яка заважає програмі працювати. Полагодьте це! :)
#Якщо ви передасте функцію - список улюблених тварин, вам слід отримати список тварин із доданими порядками та новими рядками.

# wiil use enumerate to add som strings i every (i) in the list

def list_animals(animals):
	
	an_lst = list (map(str, animals.split()))

	for (index, item) in enumerate(an_lst):  #### will diivide items # https://younglinux.info/python/for.php # enumerate генерирует пары кортежей, состоящих из индекса элемента и значения элемента
		an_lst[index] = str(index+1) + '.' + item + '\n' # (0, rhino) (1, elephant) (2, giraffe) (3, bear)	
		an_lst2 = tuple(an_lst)
		new_lst = str(an_lst2).replace('(','').replace(")",'"').replace("'", '').replace(',','').replace(' ', '').replace('.','. ')
	return new_lst

animals = input ('Select your animal list: ')
print (list_animals(animals))

# NON-RELEVANT WITH CODEWARS