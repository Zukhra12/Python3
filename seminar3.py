# Задача 2
# #Задайте список из нескольких чисел. Напишите программу, которая найдёт 
#сумму элементов списка, стоящих на нечётной позиции.
list = [1, 12, 5, 4 , 6, 2, 7, 3, 10, 18, 9]
print(list)
sum = 0
for i in range(len(list)):
    if i % 2 != 0:
        sum = sum + list[i]
print ("Сумма элементов на нечётных позициях равна: ",sum)

# Задача 2
# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.   
list = [1, 12, 5, 4 , 6, 2, 7, 3, 10, 18, 9]
print(list)
prod_list = []
for i in range((len(list)+1)//2):
    prod_list.append(list[i] * list[len(list)-1-i])
print("ПРоизведения первого и последнего элемента равна: ")
print(prod_list)

# Задача 3 
# Задайте список из вещественных чисел.Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
def list(L):
    list = []
    for i in range(L):
        n = float(input(f"Введите {i+1} элемент: "))
        list.append(n)
    return list
m = int(input("Введите количество элементов: "))
mylist = list(m)
print(mylist)
max = 0
min = 1
for i in mylist:
    if (i - int(i)) <= min:
        min = i - int(i)
    if (i - int(i)) >= max:
        max = i - int(i)  
print(max - min)

# Задача 4 
# Напишите программу, которая будет преобразовывать десятичное число в двоичное. 
num = int(input("Введите число N: "))
result = '' 
while num != 0:
    result = str(num % 2) + result
    num //= 2
print(result)

# Задача 5
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
def list(L):
    list = []
    for i in range(L):
        n = int(input(f"Введите {i+1} элемент: "))
        list.append(n)
    return list

def fibanachi(num):
    if num > -1:
        if num == 0:
            return 0
        elif num == 1:
            return 1
        else:
            return fibanachi(num - 1) + fibanachi(num - 2)
    if num <= -1:           
        return ( (-1) * (num + 1)) + fibanachi(num)

m = int(input("Введите количество элементов: "))
mylist = list(m)
print(mylist)
for i in range(len(mylist) + 1):
    mylist.append(fibanachi(i))
print(mylist)



