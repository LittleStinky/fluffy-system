import random
a = {random.randint(1, 100) for x in range(1, random.randint(1, 100))}
b = {random.randint(1, 100) for x in range(1, random.randint(1, 100))}
print("a:", a)
print("b:", b)
print("a & b:", a.intersection(b)) 
print("a - b:", a.difference(b)) 
print("b - a:", b.difference(a)) 
print("a ^ b:", a.symmetric_difference(b))
