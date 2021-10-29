# 1
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in number_list:
    print(str(number) + ' Hola!')

# 2
for number in number_list:
    if number % 2 == 0:
        print(number)
# 3
list_numbers_sum = 0
for number in number_list:
    list_numbers_sum = list_numbers_sum + number
print(list_numbers_sum)

# 4
greeting = 'Hello Python!'
for letter in greeting:
    if letter == 'o':
        print(letter)

for letter in 'Hello Python!':
    if letter != 'o':
        print(letter)

for letter in 'Hello Python!':
    print('One more letter!')

# 5
tuple_list = [('a', 'b'), ('c', 'd'), ('e', 'f')]
for item in tuple_list:
    print(item)
for letter_1, letter_2 in tuple_list:
    print(letter_1, letter_2)
for letter_1, letter_2 in tuple_list:
    print(letter_1)
    print(letter_2)

# 6
tuple_list_1 = [('a', 'b', 1), ('c', 'd', 4), ('e', 'f', 5)]
for letter_1, letter_2, number in tuple_list_1:
    print(letter_1, letter_2, number)

# 7
dictionary = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
for item in dictionary:
    print(item)
for item in dictionary.items():
    print(item)
for key, value in dictionary.items():
    print(key)
for item in dictionary.keys():
    print(item)
for item in dictionary.values():
    print(item)
for key, value in dictionary.items():
    print(value)

for x in range(5):
    print(x)

for _ in range(5):
    print('Hello!')

# 8
number = 0
for i in range(10, 31):
    if i % 2 == 0:
        number += i
print(number)

# 9
number_input = range(int(input('Введите число: ')))
for i in number_input:
    print('Hello')


