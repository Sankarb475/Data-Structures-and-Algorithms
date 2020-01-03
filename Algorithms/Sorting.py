Insertion Sort 
===================================================================
def insertion(a):
    for i in range(1,len(a)):
        for j in range(i):
            if a[i] <= a[j]:
                temp = a[j]
                a[j] = a[i]
                a[i] = temp
    return a

list1 = [1,4,7,9,2,10,19,15,12,6,10]
print(insertion(list1))
