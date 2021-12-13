def chislo_fibonacci(nomer):
    """Рекурсивная функция возвращающая заданное (номером) число Фибоначчи.
    """
    if nomer in (1, 2):
        return 1
    return chislo_fibonacci(nomer-1) + chislo_fibonacci(nomer-2)


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
    else: 
         return False

    if (flag_len == False or
            flag_digit == False or
            flag_alpha == False):
        return False
    else:
        return True


passwd = input("Введите новый пароль: ")
print(Pass(passwd))