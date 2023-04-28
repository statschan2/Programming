def solution(my_string):
    m = ['a','e','i','o','u']
    string = []
    
    for i in list(my_string) :
        if i not in m :
            string.append(i)
    
    return ''.join(string)