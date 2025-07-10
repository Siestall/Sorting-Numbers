from random import *

k = []
l = []
n = []

m = [choice([x for x in range(100)]) for x in range(randint(10,50))]

for i in range(len(m)):
    if i%2==0:
        k.append(m[i])
    else:
        l.append(m[i])

k = sorted(k)
l = sorted(l)[::-1]

for a in range(len(l)):
    n += [k[a]] + [l[a]]

print(m)
print(n)
