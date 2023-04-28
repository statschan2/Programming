def solution(a, b):
    return sum([i for i in range(b if a > b else a, (a if a > b else b) + 1)])