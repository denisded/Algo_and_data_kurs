"""
Написать программу, которая генерирует в указанных пользователем границах:
    a. случайное целое число,
    b. случайное вещественное число,
    c. случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
"""
import random
a = int(input("Введите начало диапазона целых чисел "))
b = int(input("Введите конец диапазона целых чисел "))
print(f"Случайное целое число {random.randint(a, b)}")
c = float(input("Введите начало диапазона вещественных чисел "))
d = float(input("Введите конец диапазона вещественных чисел "))
print(f"Случайное вещественное число {random.uniform(c, d)}")
e = str(input("Введите начало диапазона целых чисел "))
f = str(input("Введите конец диапазона целых чисел "))
print(f"Случайное целое число {chr(random.randint(ord(e), ord(f)))}")