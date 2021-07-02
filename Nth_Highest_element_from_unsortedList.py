You can keep two different counts for each element -- the number of elements bigger than the element, and the number of elements lesser than the element.

Then do a if check N == number of elements bigger than each element
-- the element satisfies this above condition is your output

check below solution --


def NthHighest(l,n):
    if len(l) <n:
        return 0
    for i in range(len(l)):
        low_count = 0
        up_count = 0
        for j in range(len(l)):
            if l[j] > l[i]:
                up_count = up_count + 1
            else:
                low_count = low_count + 1

        # print(l[i],low_count, up_count)
        if up_count == n-1:
            #print(l[i])
            return l[i]

# # find the 4th largest number 

l = [1,3,4,9,5,15,5,13,19,27,22]
print(NthHighest(l,4))  



-- using the above solution you can find both - `Nth highest as well as Nth Lowest` 
