l = []

for i in range(9) :
    num = int(input())
    l.append(num)
    
print(max(l))
print(l.index(max(l)) + 1)