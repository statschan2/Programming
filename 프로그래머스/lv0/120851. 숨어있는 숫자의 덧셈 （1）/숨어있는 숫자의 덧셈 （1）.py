def solution(my_string):
    answer = 0
    for i in list(my_string) :
        if ord(i) > 64 :
            pass
        else :
            answer += int(i)
    return answer