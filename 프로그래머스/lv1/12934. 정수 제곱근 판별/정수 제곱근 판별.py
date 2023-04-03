def solution(n):
    import math
    num = math.sqrt(n)
    if num % 1 == 0 :
        return (num + 1) ** 2
    else : return -1