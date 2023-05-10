def solution(d, budget):
    answer = 0
    money = budget
    
    for t in sorted(d) :
        if money < t :
            break
        else :
            money -= t
            answer += 1
    return answer