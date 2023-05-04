def solution(n):
    return sum([i if n % 2 != 0 else (i+1)**2 for i in range(1,n+1,2)])