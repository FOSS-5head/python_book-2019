# 4.7 ВЛОЖЕННЫЙ ЦИКЛ

# Эта программа усредняет оценки. Она запрашивает количество 
# студентов и количество оценок в расчете на студента.

# Получить количество студентов.
num_students = int(input('Сколько у вас студентов? '))

# Получить количество оценок в расчете на студента.
num_test_scores = int(input('Сколько оценок в расчете на студента? '))

# Опеределить средний балл каждого студента.
for student in range (num_students):
    # Инициализировать накопитель оценок.
    total = 0.0
    # Получить оценки за лабораторные работы.
    print('Номер студента', student +1)
    print('-----------------')
    for test_num in range (num_test_scores):
        print('Номер лабораторной работы', test_num + 1, end = '')
        score = float(input(': '))
        # Прибавить оценку в накопитель.
        total += score

    # Рассчитать средний балл этого студента.
    average = total / num_test_scores

    # Показать средний балл.
    print('Средний балл студента номер', student + 1,
        'составляет:', average)

    print()