# https://www.geeksforgeeks.org/move-negative-numbers-beginning-positive-end-constant-extra-space/?ref=leftbar-rightbar

# Moving all the negatives in front of the list with constant space

arr = [-12, 11, -13, -5, 6, -7, 5, -3, -6,7,6,-12]

# O(N)
j = 0
for i in range(len(arr)):
    if arr[i] < 0:
        arr[i], arr[j] = arr[j], arr[i]
        j = j + 1
        
print(arr)


# O(N^2)
for i in range(len(arr)):
    if arr[i] > 0:
        for j in range(i+1, len(arr)):
            if arr[j] < 0:
                arr[i], arr[j] = arr[j], arr[i]
                break
            
print(arr)           

        

# this is not constant space, but this faster
temp = arr.copy()
print(temp)
for index,val in enumerate(arr):
    if val>0:
        temp.remove(val)
        temp.append(val)
        
print(temp)
     
        
        
    




