def solution(s):
    list_answer = []
    string = s.lower().split(' ')
    
    for i in range(len(string)) :
        if string[i] == '' :
            list_answer.append(string[i])
        else :
            list_answer.append(string[i].capitalize())
            
    return ' '.join(list_answer)
    