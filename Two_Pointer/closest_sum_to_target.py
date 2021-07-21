# Given a sorted array and a number x, find the pair in array whose sum is closest to x
# https://www.geeksforgeeks.org/given-sorted-array-number-x-find-pair-array-whose-sum-closest-x/

# my solution O(N^2)
a = [1, 3, 4, 7, 10]
x = 15
# 22 and 30

closest_val = 0 
val1 = val2 = 0
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if abs(x-closest_val) > abs(x-a[i] -a[j]):
            closest_val = a[i] + a[j]
            val1 = a[i]
            val2 = a[j]
        
print(val1,val2,closest_val)
            
        
    
    
# Two pointer solution - the list has to be sorted 
a = [1, 3, 4, 7, 10]
x = 15
# 22 and 30

diff = max(a)
val1 = val2 = 0
i = 0
j = len(a) - 1

while i < j:
    if abs(a[i] + a[j] - x) < diff:
        diff = abs(a[i] + a[j] - x)
        val1 = a[i]
        val2 = a[j]
        
    if (a[i] + a[j]) > x:
        j = j - 1
        
    else:
        i = i + 1
        
print(val1, val2, diff)
        
            
        
        
        












        

