def solution(price, money, count):
    total = 0
    for i in range(count) :
        total += (price * (i+1))
    if money < total :
        answer = total - money
    else :
        answer = 0
    return answer