"""
Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, надо вывести 6843
"""
import timeit
import cProfile


def revers(a):
    a_list = list(str(a))
    a_list.reverse()
    a1 = "".join(a_list)
    return a1


a = 3294
# print(timeit.timeit(revers(a)))
# timeit 0.026846399999999992

cProfile.run(revers(a))
# cprofile 3 function calls in 0.000 seconds