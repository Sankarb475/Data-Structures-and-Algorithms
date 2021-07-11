How to merge/append two sorted python list into one sorted python list with O(n) time complexity
=========================================================================================================

a = [1,3,4,7,8,11,15,17]

b = [2,5,13,19,33]

len_a = len(a)
len_b = len(b)
out_list = []
i = j = 0
while i < len_a or j < len_b:
    if i >= len_a:
        out_list.extend(b[j:])
        break
    if j >=len_b:
        out_list.extend(a[i:])
        break
        
    if a[i] > b[j]:
        out_list.append(b[j])
        j = j + 1
    elif a[i] < b[j]:
        out_list.append(a[i])
        i = i + 1
        
    elif a[i] == b[j]:
        out_list.append(a[i])
        i = i + 1
        j = j + 1
        
print(out_list)
        
-- the above code is for merging, that is duplicate elements will be removed.
-- to main duplicate list add this below line in a[i] == b[j] elif condition.

out_list.append(b[j])





