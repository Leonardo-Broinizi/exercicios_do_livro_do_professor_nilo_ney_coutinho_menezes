'''a = [1,2,3,4,5,6,7,8,9,10]
b = [11,2,33,4,55,6,77,8,99,10]
c = d = 0
e = a[:]
while c < len(a):
    while True and d < len(b):
        if b[c] == a[d]:
            break
        d += 1
    if b[c] != a[d]:
        e.append(b[c])
    c += 1
    d = 0
print(e)'''

l1 = ['a', 'b', 'c', 'd', 'e']
l2 = ['f', 'g', 'a', 'd', 'h']
l3 = l1[:]
c1 = c2 = 0
while c1 < len(l1):
    while True:
        if l1[c2] == l2[c1]:
            break
        elif c2+1 == len(l2):
            l3.append(l2[c1])
            break
        c2 += 1
    c2 = 0
    c1 += 1
print(l3)