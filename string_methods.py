name = input('Введите Ваше имя: ')
current_year = 2024
date_of_birth = input('В каком году вы родились? ')
age = current_year - int(date_of_birth)
print('Здравствуйте, ', name)
print('В этом году вам', age, 'лет')

# регистры строк
print('привет, я СТРОКА в неопределённом РЕГИСТРЕ')
print('привет, я СТРОКА в неопределённом РЕГИСТРЕ'.upper())
print('привет, я СТРОКА в неопределённом РЕГИСТРЕ'.lower())
print('привет, я СТРОКА в неопределённом РЕГИСТРЕ'.replace(' ' , ''))