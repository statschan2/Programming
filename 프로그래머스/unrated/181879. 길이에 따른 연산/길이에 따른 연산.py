def solution(num_list):
    from functools import reduce
    return sum(num_list) if len(num_list) > 10 else reduce(lambda x, y : x*y,num_list)