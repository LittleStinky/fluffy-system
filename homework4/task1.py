import random
list_sort = [random.randint(1, 100) for x in range(1, random.randint(1, 10))] 
print(list_sort)
f = True
count = 1
while f:
    f = False
    for i in range(len(list_sort) - count) :
        if list_sort[i] > list_sort[i + 1] :
            c = list_sort[i]
            list_sort[i] = list_sort[i + 1]
            list_sort[i + 1] = c
            f = True
    count += 1
print("Отсортированный массив:", list_sort)
