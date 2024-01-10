# Створити структуру даних для студентів з імен та прізвищ, можна випадкових. Придумати структуру даних,
# щоб вказувати, у якій групі навчається студент (Групи Python, FrontEnd, FullStack, Java).
# Студент може навчатися у кількох групах. Потім вивести:
# студентів, які навчаються у двох та більше групах
# студентів, які не навчаються на фронтенді
# студентів, які вивчають Python або Java


#
students = {
    "Vadimov Vadim": ["Python", "FrontEnd", "FullStack", "Java"],
    "Antonov Anton": ["Python"],
    "Maksimov Maksim": ["Python", "FrontEnd"],
    "Romanov Roman": ["Python", "Java"],
    "Ruslanov Ruslan": ["Java"],
    "Bohdanov Bohdan": ["FrontEnd", "FullStack", "Java"],
    "Markina Marina": ["FullStack"],
    "Vinnik Olha": ["FrontEnd", "FullStack"],
    "Abramova Polina": ["Python", "FrontEnd", "FullStack"]

}

a = filter(lambda x: len(x[1]) > 2, students.items())

print("Студенти, які навчаються у двох та більше групах: ", end=" ")

for i in a:
    print(i[0], end=", ")

print("\n")


b = filter(lambda x: "FrontEnd" not in x[1], students.items())
print("Студенти, які не навчаються на FrontEnd: ", end=" ")


for i in b:
    print(i[0], end=", ")


print("\n")

c = filter(lambda x: "Python" in x[1] or "Java" in x[1], students.items())
print("Студенти, які вивчають Python або Java: ", end=" ")

for i in c:
    print(i[0], end=", ")







python_students = []

for key, value in students.items():
    if "Python" in value:
        python_students.append(key)

print(python_students)

