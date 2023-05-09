def solution(left, right):
    n = []
    answer = 0
    for i in range(left, right+1) :
        for j in range(1, i+1) :
            if i % j == 0 :
                n.append(j)
        if len(n) % 2 == 0 :
            answer += i
        else :
            answer -= i
        n = []
    return answer