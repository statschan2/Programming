# A, B, C
a, b, c = map(int, input().split())

# (A+B)%C
print((a+b)%c)

# ((A%C) + (B%C))%C
print(((a%c) + (b%c))%c)

# (A×B)%C
print((a*b)%c)

# ((A%C) × (B%C))%C
print(((a%c) * (b%c))%c)