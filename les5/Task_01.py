"""
Пользователь вводит данные о количестве предприятий, их наименования и
    прибыль за четыре квартала для каждого предприятия.
        Программа должна определить среднюю прибыль (за год для всех предприятий) и
        отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
"""


from collections import deque

count = int(input("Введите количество предприятий "))
allfactory = []
for i in range(count):
    allfactory.append(
        {"name": input("Введите название предприятия "),
         "avg_profit": int(input("Введите прибыль за 4 квартала "))
         }
    )

avg_profit_all = 0
for i in allfactory:
    avg_profit_all += i.get("avg_profit")
avg_profit_all = avg_profit_all / count
print(f"Средняя прибыль предприятий = {avg_profit_all}")
deq_dowm = deque()
deq_up = deque()
for i in allfactory:
    if i.get("avg_profit") > avg_profit_all:
        deq_up.append(i.get("name"))
    elif i.get("avg_profit") < avg_profit_all:
        deq_dowm.append(i.get("name"))

print(f"Предприятия с доходностью ниже среднего: {deq_dowm}")
print(f"Предприятия с доходностью выше среднего: {deq_up}")