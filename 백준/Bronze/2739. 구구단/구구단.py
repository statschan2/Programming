# 단
n = int(input())

# n단
for i in range(9) :
    print('{:d} * {:d} = {:d}'.format(n, (i+1), n*(i+1)))