# 정수 x
x = int(input())

# 정수 y
y = int(input())

# 사분면 번호
if x > 0 :
    if y > 0 : print(1)
    elif y < 0 : print(4)
elif x < 0 :
    if y > 0 : print(2)
    elif y < 0 : print(3)