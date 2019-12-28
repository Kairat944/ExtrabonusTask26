import random
a = []
for i in range(20):
    a.append(int(random.random() * 20) - 10)
print(a)
neg = []
pos = []
for i in a:
    if i < 0:
        neg.append(i)
    elif i > 0:
        pos.append(i)
print(neg)
print(pos)