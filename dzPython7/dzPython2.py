#1
print("Введите два числа(можно дробные): ")
first_number = float(input())
second_number = float(input())
print("Результат сложения чисел: ", first_number + second_number)
print("Результат вычитания чисел: ", first_number - second_number)
print("Результат умножения чисел: ", first_number * second_number)
print("Результат деления чисел: ", first_number / second_number)
print("Результат возведения в степень чисел: ", first_number ** second_number)
print("Результат деления по модулю чисел: ", first_number % second_number)
print("Результат целочисленного деления чисел: ", first_number // second_number)

#2
print("Введите ваше имя: ")
name = input()
print("Здравствуйте, %s, рады знакомству!!!1!111!1!!" %(name))

#3
print("Введите любую строку: ")
print("Выводим последние два символа этой строки в обратном порядке:", input()[-1:-3:-1])

#4
import math

print("Введите радиус круга: ")
radius = float(input())
print("Площадь круга = ", math.pi * radius**2)
