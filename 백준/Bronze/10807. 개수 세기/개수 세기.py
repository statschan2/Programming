n = int(input())
a = map(int,input().split())
v = int(input())
s = 0

for i in a :
    if i == v :
        s += 1
    else :
        s += 0
        
print(s)