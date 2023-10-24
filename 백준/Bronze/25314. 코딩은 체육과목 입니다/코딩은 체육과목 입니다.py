N = int(input())

sum = 0
if N % 4 == 0 :
    for i in range(N//4) :
        sum += 1
    
    print('long ' * sum + 'int')