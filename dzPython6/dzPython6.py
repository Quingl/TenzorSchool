#1
# def bytein(stroki):
#     str_contain = list()

#     for i in range(len(stroki)):
#         print("\n")
#         str_contain.append(stroki[i].encode("utf-8"))
#         print("Преобразовали строку к типу: ", type(str_contain[i]))
#         for j in str_contain[i]:
#             print(j, end= '')
 
#     byteout(str_contain)

# def byteout(str_contain):
#     byteo = list()

#     for i in range(len(str_contain)):
#         print("\n")
#         byteo.append(str_contain[i].decode())
#         print("Преобразовали байт код обратно к типу: ", type(byteo[i]))
#         print("Строка преобразованная из байт кода: ", byteo[i])

# print("Введите строки: ")


# stroki = input().split()
# bytein(stroki)

# 2
# try:
#     with open('C:\RepoGitKraken\TenzorSchool\dzPython6\input.txt', 'r') as input:

#         values = input.read().split()
#         itog = list()
#         if int(values[0]) >= 2 and int(values[1]) >= 6 and int(values[2]) >= 1:
#             itog.append(int(values[0]) // 2)
#             itog.append(int(values[1]) // 6)
#             itog.append(int(values[2]) // 1)
#             itog.sort()
#             with open('C:\RepoGitKraken\TenzorSchool\dzPython6\output.txt', 'w') as out:
#                output = out.write(str(itog[0]))
#         else:
#             with open('C:\RepoGitKraken\TenzorSchool\dzPython6\output.txt', 'w') as out:
#                 output = out.write('0')
# except IndexError:
#     print("Файл input.txt пуст!")


#3
def xor(s, key):
    uncript_str = ""
    for i in range(len(s)):
        uncript_str += chr(ord(s[i]) ^ key)
    return  uncript_str    
 
with open('C:\RepoGitKraken\TenzorSchool\dzPython6\input2.txt', 'r', encoding="UTF-8") as input:
    string = input.readline()
    key = int(input.readline())
    xstr = xor(string, key) 
    with open('C:\RepoGitKraken\TenzorSchool\dzPython6\output2.txt', 'w', encoding="UTF-8") as out:
        output = out.write("Начальная строка: {a} ".format(a = string))
        output = out.write("Зашифрованная строка: {a} ".format(a = xstr))
        output = out.write("Расшифрованная строка:{a} ".format(a = xor(xstr, key)))