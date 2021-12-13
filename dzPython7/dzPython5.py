#1

def Pass(passwd):
    """Проверка пароля:
    не менее 6 символов,
    есть хоть одно число,
    есть символ алфавита,
    нет слова "password" в любом регистре.
    """
    flag_len = bool(False)
    flag_digit = bool(False)
    flag_alpha = bool(False)

    if len(passwd) >= 6  and "password" not in (passwd.lower()):
        flag_len = bool(True)
    
    for i in range(len(passwd)):

        if passwd[i].isdigit():
            flag_digit = bool(True)
            continue 

        if passwd[i].isalpha():
            flag_alpha = bool(True)
            continue

    if (flag_len == False or
            flag_digit == False or
            flag_alpha == False):
        return False
    else:
        return True


passwd = input("Введите новый пароль: ")
print(Pass(passwd))


#2
def Any(*digits):
    """Суммируем любое количество чисел.
    """
    count = 0

    for i in range(len(digits[0])):
        count += digits[0][i]
    return count

print("Введите сколько угодно чисел через пробел: ")

try:
    digits = list(map(int, input().split()))
    print(Any(digits))
except:
    print("Введите числа!")


#3
def chislo_fibonacci(nomer):
    """Рекурсивная функция возвращающая заданное (номером) число Фибоначчи.
    """
    if nomer in (1, 2):
        return 1
    return chislo_fibonacci(nomer-1) + chislo_fibonacci(nomer-2)

print("Введите порядковый номер числа Фибоначчи: ")
try:
    nomer = int(input())
    print("Число Фибоначчи с порядковым номером %a ="%(nomer), chislo_fibonacci(nomer))
except:
        print("Введите целое число!")
