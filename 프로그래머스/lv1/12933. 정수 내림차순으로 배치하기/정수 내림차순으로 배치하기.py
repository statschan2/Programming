def solution(n):
    num_list = list(map(int,str(n)))
    num_list.sort(reverse = True)
    return int(''.join(map(str,num_list)))