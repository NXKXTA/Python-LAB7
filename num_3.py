s1 = input("Введите набор чисел 1: ")
s2 = input("Введите набор чисел 2: ")

if not s1.isdigit() or not s2.isdigit():
    print("Вы ввели не натуральное число")
else:
    s1 = set(s1)
    s2 = set(s2)

    res = s1.intersection(s2)
    print("Цифры, которые встречаются в обоих числах: ", res)
