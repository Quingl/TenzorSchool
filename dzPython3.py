#1
# location = [0, 0]

# for i in range(1):
#     word = list(input().split())
#     word[1] = float(word[1])
#     if word[0] == "вверх" and word[1] >= 0:
#         location[1] += word[1]
#     elif word[0] == "вниз" and word[1] >= 0:
#         location[1] -= word[1]
#     elif  word[0] == "вправо" and word[1] >= 0:
#         location[0] += word[1]
#     elif word[0] == "влево" and word[1] >= 0:
#         location[0] -= word[1]
#     else:
#         print("Вы ввели недопустимые значения!")
#     print("Наш ввод:", word)

# print("Координаты персонажа:", location)

#2
# from math import sqrt


# location = [0, 0]
# i = True

# while i == True:
#     print("Куда пойдет ваш персонаж, сколько сделает шагов?")
#     word = input().split()
#     if word[0] == "вверх" and float(word[1]) >= 0:
#         location[1] += float(word[1])
#         print("Координаты персонажа:", location)
#     elif word[0] == "вниз" and float(word[1]) >= 0:
#         location[1] -= float(word[1])
#         print("Координаты персонажа:", location)
#     elif  word[0] == "вправо" and float(word[1]) >= 0:
#         location[0] += float(word[1])
#         print("Координаты персонажа:", location)
#     elif word[0] == "влево" and float(word[1]) >= 0:
#         location[0] -= float(word[1])
#         print("Координаты персонажа:", location)
#     elif word[0] == "стоп":
#         i = False
#     else:
#         print("Вы ввели недопустимые значения!")

#8
# import math
# print("Введите коэффициенты через пробел:")
# equation = list(map(float, input().split()))
# diskriminant = equation[1]**2 - 4 * equation[0] * equation[2]
# if equation[0] == 0.0:
#     print("Уравнение линейное!")
# elif diskriminant > 0:
#     x1 = (-equation[1] - (diskriminant)**0.5)/(2 * equation[0])
#     x2 = (-equation[1] + (diskriminant)**0.5)/(2 * equation[0])
#     print(x1, x2)
# elif diskriminant == 0.0:
#     x = -equation[1]/(2 * equation[0])
#     print(x)
# elif diskriminant < 0:
#     print("Решений нет!")
# else:
#     print("Вы ввели недопустимые значения коэффициентов!")

#4
print("Введите коэффициенты через пробел:")
equation =  input().split()
a = complex(equation[0])
b = complex(equation[1])
c = complex(equation[2])
diskriminant = b**2 - 4 * a * c
if a == 0.0:
    print("Уравнение линейное!")
elif diskriminant != 0:
    x1 = (-b - (diskriminant)**0.5)/(2 * a)
    x2 = (-b + (diskriminant)**0.5)/(2 * a)
    x1 = complex(round(x1.real, 8), round(x1.imag, 8))
    x2 = complex(round(x2.real, 8), round(x2.imag, 8))
    if x1.imag == 0.0:
        x1 = x1.real
    if x2.imag == 0.0:
        x2 = x2.real
    print(x1, x2)
elif diskriminant == 0.0:
    x = -b/(2 * a)
    x = complex(round(x.real, 8), round(x.imag, 8))
    print(x)
else:
    print("Вы ввели недопустимые значения коэффициентов!")

