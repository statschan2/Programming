def d(n) :
    num = n
    for i in list(str(n)) :
        num += int(i)
    return num

l = []
s = []

for i in range(1, 10001) :
    l.append(d(i))
    
for i in range(1, 10001) :
    if i not in l :
        print(i)