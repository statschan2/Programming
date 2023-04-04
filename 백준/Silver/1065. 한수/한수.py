n = int(input())
x = 0

for i in range(1, n + 1) :
    if i < 100 :
        x += 1
    else :
        h = list(str(i))
        if (int(h[0]) - int(h[1])) == (int(h[1]) - int(h[2])) :
            x += 1
        else :
            x = x
            
print(x)