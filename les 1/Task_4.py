"""
Пользователь вводит две буквы.
Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
"""
a = str(input("Введите 1 букву алфавита "))
b = str(input("Введите 2 букву алфавита "))
print(f"Место 1 буквы в алфавите {ord(a)-96}")
print(f"Место 2 буквы в алфавите {ord(b)-96}")
print(f"Между буквами {(ord(b)-96) - (ord(a)-96)} символ(ов)")