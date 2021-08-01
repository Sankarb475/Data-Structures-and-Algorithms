https://www.geeksforgeeks.org/minimum-number-swaps-required-sort-array/
  
# Straight forward solution
arr = [1,5,4,3,2]
count = 0
def swap(arr,i,j):
    temp = arr[j]
    arr[j] = arr[i]
    arr[i] = arr[j]
    
def minswap(arr):
    temp = arr.copy()
    temp = sorted(temp)
    count = 0
    for i in range(len(arr)):
        if arr[i] != temp[i]:
            count = count + 1
        
        swap(arr,i,arr.index(temp[i]))
        
    print(count)
        
    
minswap(arr)  


# Graph solution



    
    
  
  
