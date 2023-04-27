def solution(x):
    num_sum = 0
    for i in range(len(list(str(x)))) :
        num_sum += int(list(str(x))[i])
    return True if x % num_sum == 0 else False