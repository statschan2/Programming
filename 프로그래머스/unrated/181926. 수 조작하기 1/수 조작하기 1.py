def solution(n, c):
    for i in range(len(c)) :
        if c[i] == 'w' :
            n += 1
        elif c[i] == 's' :
            n -= 1
        elif c[i] == 'd' :
            n += 10
        elif c[i] == 'a' :
            n -= 10
    return n