"""
Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, надо вывести 6843
"""
import timeit
import cProfile

def revers(a):
    rev = ""
    while a > 0:
        rev = rev + str(a % 10)
        a //= 10
    return rev


a = 3294
# print(timeit.timeit(revers(a)))
# timeit 0.026155499999999998

cProfile.run(revers(a))
# cprofile 3 function calls in 0.000 seconds