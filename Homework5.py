# Створити словник оцінок передбачуваних студентів (Ключ – ПІ студента, значення – список оцінок студентів).
# Знайти найуспішнішого і самого слабенького за середнім балом.

students = {
    "Vadimov Vadim": [8, 11, 9],
    "Antonov Anton": [7, 12, 9, 8, 10, 5],
    "Maksimov Maksim": [5, 12, 9, 10, 8, 7],
    "Romanov Roman": [10, 8, 11, 6, 7, 9],
    "Ruslanov Ruslan": [9, 6, 8, 10, 7, 5],
    "Bohdanov Bohdan": [6, 10, 8, 7, 9, 12],
    "Markina Marina": [10, 6, 5, 9, 8, 11],
    "Vinnik Olha": [10, 8, 6, 9, 5, 11],
    "Abramova Polina": [11, 7, 9, 10, 6, 8]

}
def average_grade(students_grades:dict):
    average_grades = dict()
    for key, value in students.items():
        grade = sum(value)
        avarage = round(grade / len(value), 1)
        average_grades.update({key: avarage})

    minimum_grade = min(average_grades.items(), key = lambda x: x[1])
    maximum_grade = max(average_grades.items(), key = lambda x: x[1])
    return minimum_grade, maximum_grade


    print(average_grades.items())

    print(average_grades)
    print(minimum_grade)
    print(maximum_grade)



print(average_grade(students))


average_grade(students)


# Найуспішніший студент
min_students = average_grade(students)[0]
max_students = average_grade(students)[1]
print(f"Самий слабенький студент є {min_students[0]} з оцінкою {min_students[1]}")
print(f"Найуспішніший студент є {max_students[0]} з оцінкою {max_students[1]}")












