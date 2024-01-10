# # Завдання 1
# # Написати 2 функції. Перша функція прийматиме рядок та приводитиме його до нижнього регістру.
# # Друга функція прийматиме рядок та приводитиме його до верхнього регістру.
# #
# Головна програма має застосовувати обидві функції до списку рядків за допомогою map,
# для кожного з рядків, та друкувати результат.

def lower_case(string: str):
    new_string = ""

    for i in string:
        new_string += i.lower()
    return new_string

def upper_case(string: str):
    new_string = ""

    for i in string:
        new_string += i.upper()
    return new_string


test_string = "HellLO World"
a = map(lower_case, test_string)

clear_str = ""
for i in a:
    clear_str += i
print(clear_str)

b = map(upper_case, test_string)

clear_str = ""
for i in b:
    clear_str += i
print(clear_str)




print("--------------------")

# Написати функцію, яка буде підносити число у квадрат. Написати другу, яка буде перевіряти, чи є число простим.
# Потрібно видрукувати в головній програмі квадрати усіх простих чисел зі списку від 0 до 50 за допомогою map

def square_num(number):
    return number ** 2

def simple_num(input_number: int):
    list_div = []
    for i in range(2, input_number + 1):
        if not input_number % i:
            list_div.append(i)
    if len(list_div) == 1:
        return True
    else:
        return False

numbers = [i for i in range(51) if simple_num(i)]
numbers = list(map(square_num, numbers))

print(numbers)

