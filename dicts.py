phone_book = {'Oleg': [+79507451234, 89197451234], 'Vladimir': +79507451235}
print(phone_book)
phone_book['Oleg'][1] = +79197451234
print(phone_book['Oleg'])
phone_book['Anton'] = False
print(phone_book)
del phone_book['Anton']
print(phone_book)

phone_book.update({'Sasha': 1234,
                   'Masha': 4321})
print(phone_book)

print(phone_book.get(input('Введите имя: '), 'Такого имени нет в книге'))

a = phone_book.pop('Masha')
print('Masha = ', a, phone_book)

print(phone_book.keys())

print(phone_book.values())

print(phone_book.items())


set_ = {1,2,3,4,5,1,2,3,6,6,1,2,0, 'string', True, False, (1,2,3)}
list_ = [7,2,3,4,5,7,2,3,6,6,7,2, 'string', True, False, (1,2,3)]
print(set_)
list_ = set(list_)
print(list_)
list_.discard(True)
print(list_)
list_.discard(False)
print(list_)
list_.add(True)
print(list_)
list_.remove((1,2,3))
print(list_)
b = list_.pop()
print(b, list_)
c = list_.pop()
print(c, list_)