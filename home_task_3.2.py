# task2 - SoftServe#4 - Lesson4

# 1 Роздрукувати всі непарні числа менші 100. (написати два варіанти коду: один використовуючи оператор continue, а інший без цього оператора).
# 2.1.1 # із застосуванням 'сontinue' всі непарні числа
a = 0
while a <= 99: # так як ми виводимо непарні числа то останнім непарним є - 99
	a += 1 
	if (a % 2) == 0: # ділення по модулю на парне число - буде дорівнювати 0 # далі нулі пропускаємо використовуючи continue
		continue # пропустить всі парні числа
	print (a)

# 2.1.2 із застосуванням 'сontinue' всі парні числа
a = 0 
while a <= 100: # останнім парним є - 99
	a += 1 
	if (a % 2) == 1: # # ділення по модулю на парне число - буде дорівнювати 1 # далі одиниці пропускаємо використовуючи continue
		continue # пропустить всі непарні числа
	print (a)

# 2.2.1 без застосування 'сontinue' всі парні числа
for a in range(1, 100, 2): # 1 - початок діапазону, 100 -кінець діапазону, 2 - хід діапазону
	print (a)

# 2.2.2 із застосуванням від'ємного значення
for a in range(2, 101):
	a = a - 1
	if (a % 2) == 1:
		print (a)
	else:
		pass

# 2.2.3 із застосуванням від'ємного значення
for a in range(3, 102):
	a = a - 2
	if (a % 2) != 0:
		print (a)
	else:
		pass

# 2.2.4 із формуванням зі списку

numbers = list ( range ( 1, 100, 1 ))
numbers_slice = numbers [:100:2] 

tpl_lst = tuple ( numbers_slice )

strings = [str(integer) for integer in tpl_lst] ### converting to string from TUPLE∕LIST∕CORTEGE∕DICTIONARY
a_string = " ".join(strings)
an_integer = str(a_string)

print ( an_integer ) # видасть набір чисел в форматі кортежа










