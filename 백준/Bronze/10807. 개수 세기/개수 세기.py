# 정수의 개수 N
n = int(input())

# 공백으로 구분된 정수
num_list = list(map(int, input().split()))[:n]

# 찾으려고 하는 정수
v = int(input())

# 주어진 n개의 정수 중 v의 갯수
print(num_list.count(v))