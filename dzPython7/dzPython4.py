#1
import random

def sort(sort_arr):
    """Сортировка Пузырьком.
    """
    N = len(arr)
    
    for i in range(N - 1):
        for j in range(N - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return print("Конечный (отсортированный методом пузырька) список:", arr)

n = random.randint(5, 20)  #рандомно генерируем длину списка от 5 до 20
arr = list(range(n))  #создаем список с длиной списка выше
random.shuffle(arr)  #рандомно перемешиваем числа в списке
print("Начальный массив заполненный рандомно:", arr)
sort(arr)

#2
dictionary = {'orange':(252, 126, 8),
              'pink':(252, 8, 244),
              'blue':(28, 8, 252),
              'green':(8, 252, 32),
              'yellow':(220, 252, 8) }
print(dictionary.items())

#3
import random

# spisok_1 = {i ** 2 for i in range(10)}
# spisok_2 = {i ** 2 for i in range(15)}

spisok_1 = {1, 5, 3, 
            4, 2
            }
spisok_2 = {6, 4, 5,
            3, 7
            }
print(spisok_1)
print(spisok_2)
print(set.intersection(spisok_1, spisok_2))  #Входят в оба множ-ва
print(spisok_1.difference(spisok_2))  #входят в первое, но не во второе
print(spisok_2.difference(spisok_1))  #входят во второе, но не в первое
print(spisok_1.symmetric_difference(spisok_2))  #входят в первое или второе, но не в оба одновременно

#4
def Add(inventory ,item, weight):
    """Добавляем предмет в инвентарь.
    """

    inventory.update({item[0] : int(item[1])})
    print(inventory)
    print(weight)
        

inventory = dict()
weight = 0
max_weight = 35

while True:
    yes_or_no = input("Добавить предмет - add, удалить предмет - remove, quit - выйти: ")
    if yes_or_no == 'add':
        print("Введите название предмета и его вес")
        item = input().split()
        if item[1].isdigit():
            if max_weight-weight >= int(item[1]):
                weight += int(item[1])
                Add(inventory, item, weight)
            else:
                print("осталось места:", max_weight - weight)
                print("Места в инвентаре не хватает, добавьте другой предмет или удалите старые!", inventory)
        else:
            print("Ввод некорректен!")
    elif yes_or_no == 'remove':
        print("Введите предмет который хотите удалить:")
        item = input()
        print(inventory.pop(item))
        print(inventory)    
    elif yes_or_no == 'quit':
        print(inventory)
        print(weight)
        break
    else:
        print("Ввод некорректен!")
        

