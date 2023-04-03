def solution(s):
    num_list = [int(i) for i in s.split()]    
    return str(min(num_list)) + ' ' + str(max(num_list))