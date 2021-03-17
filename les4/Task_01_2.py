"""
Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, надо вывести 6843
"""
import timeit
import cProfile


def revers(a):
    a1 = str(a)[::-1]
    return a1


a = 3294
# print(timeit.timeit(revers(a)))
# timeit 0.12989190000000006

cProfile.run(revers(a))
# cprofile 3 function calls in 0.000 seconds