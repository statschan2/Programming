def solution(a, s):
    return sum([a[i] if s[i] == True else -a[i] for i in range(len(a))])