n_list = list(map(int, input().split()))

n_list2 = []
for i in n_list :
    n_list2.append(i*i)
    
print(sum(n_list2)%10)