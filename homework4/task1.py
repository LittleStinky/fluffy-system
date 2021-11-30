import random
l = [random.randint(1, 100) for x in range(1, random.randint(1, 10))] 
print(l)
f = True
count = 1
while f:
    f = False
    for i in range(len(l)-count) :
        if l[i] > l[i+1] :
            c = l[i]
            l[i] = l[i+1]
            l[i+1] = c
            f = True
    count += 1
print("Отсортированный массив:", l)
