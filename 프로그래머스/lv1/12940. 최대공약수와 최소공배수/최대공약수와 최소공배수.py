def solution(n, m):
    import math
    def lcm(n,m):
        return (n*m) // math.gcd(n,m)
    return [math.gcd(n, m), lcm(n, m)]