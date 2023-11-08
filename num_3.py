def is_natural_and_positive(num):
    if num.isnumeric() and int(num) > 0:
        try:
            num = int(num)
            return True
        except ValueError:
            print("Введено не натуральное число")
            exit()
    print("Введено не натуральное число")
    exit()


result = []
line_1 = input("Введите строку 1: ")
is_natural_and_positive(line_1)
line_2 = input("Введите строку 2: ")
is_natural_and_positive(line_2)
# Проверка на отсутствие вхождений i из 1-й строки во 2-ю
for i in set(line_1):
    if line_2.count(i) > 0:
        result.append(i)

# Вывод результата проверки
if len(result) == 0:
    print("Чисел из первой строки нет во второй")
    exit()
print(f"Числа присутствующие в обоих строках:\n{result}")
