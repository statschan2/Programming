def solution(n):
    num_list = []
    for i in range(n+1) :
        if i % 2 == 0 :
            num_list.append(i)
    return sum(num_list)