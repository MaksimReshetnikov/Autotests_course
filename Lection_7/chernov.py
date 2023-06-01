count = 0
subdivision = ('Разработка', 'УК', 'Нефункциональное тестирование', 'Автотестирование')
my_str = ' -> '.join((subdivision))

print(my_str)
print(type(my_str))
"""
my_dict = {letter: my_str.count(letter) for letter in my_str}    #Создадим словарь ключь - буква, значение - количество вхождений в строку my_str

sorted_my_dict = sorted(my_dict.values(), reverse=True)     #Отсортируем значения в ловаре по возрастанию
result_my_zp = 1337 * self.age * sum(sorted_my_dict[:3])
print(my_dict)
print(sorted_my_dict)

1337 * Возраст * суммарное
"""

