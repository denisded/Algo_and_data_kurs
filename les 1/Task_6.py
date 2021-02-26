"""
По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника,
составленного из этих отрезков. Если такой треугольник существует, то определить,
является ли он разносторонним, равнобедренным или равносторонним.
"""
a = int(input("Введите длину 1 стороны "))
b = int(input("Введите длину 2 стороны "))
c = int(input("Введите длину 3 стороны "))
if a >= b + c or b >= a + c or c >= a + b:
    print("Треугодльник невозможен")
elif a!=b!=c:
    print("Треугодльник разносторонний")
elif a==b==c:
    print("Треугодльник равносторонний")
else:
    print("Треугодльник равнобедренный")
