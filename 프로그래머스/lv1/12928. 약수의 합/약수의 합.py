def solution(n):
    l = []
    for i in range(1,n+1) :
        if int(n) % i == 0 :
            l.append(i)
    answer = sum(l)
    return answer