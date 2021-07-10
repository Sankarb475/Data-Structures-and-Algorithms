Approach 1 - Brute force 
===================================================================
a = [3, 10, 2, 1, 20]

lis = lis_max = 0

for i in range(len(a)):
    lis = 1
    temp_max = a[i]
    for j in range(i+1,len(a)):
        if temp_max < a[j]:
            lis = lis + 1
            temp_max = a[j]
    if lis > lis_max:
        lis_max = lis
        
print(lis_max) 

















