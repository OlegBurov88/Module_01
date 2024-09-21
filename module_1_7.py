grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

#students = list(students)
#students.sort()
students = sorted(students) # аналог строки  3 и 4

#def average(*args): return([sum(x) / len(x) for x in args])
#grades_average = list(average(*grades))
grades_average = []
for num in grades :
    average = sum(num) / len(num)
    grades_average.append(average)

students_average = dict(zip(students, grades_average))
print(students_average)