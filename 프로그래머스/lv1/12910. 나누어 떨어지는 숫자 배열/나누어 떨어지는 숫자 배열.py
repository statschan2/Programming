def solution(arr, divisor):
    return [-1] if [i for i in sorted(arr) if i % divisor ==0] == [] else [i for i in sorted(arr) if i % divisor ==0]