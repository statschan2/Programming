def solution(num_list):
    return int(''.join(map(str, [i for i in num_list if i % 2 == 1]))) + int(''.join(map(str, [i for i in num_list if i % 2 == 0])))