my_dict = {'Oleg': 1988, 'Alex': 1990, 'Anton': 1982, 'Denis': 2000}
print(my_dict)
print(my_dict['Oleg']) #print(my_dict.get(input('Введите имя: '), 'Такого имени нет'))
print(my_dict.get('Kira'))
my_dict.update({'Sasha': 1995, 'Masha': 2005})
print(my_dict.pop('Anton'))
print(my_dict)

my_set = {False, True, 'Яблоко', 2,3,4,5,6, True, False, 7,6,5,4,1.1}
print(my_set)
my_set.add(8)
my_set.add((0, 1))
my_set.remove(True)
print(my_set)