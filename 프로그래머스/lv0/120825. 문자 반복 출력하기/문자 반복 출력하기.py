def solution(my_string, n):
    str_list = []
    for i in list(my_string) :
        str_list.append(i * n)
    return ''.join(str_list)