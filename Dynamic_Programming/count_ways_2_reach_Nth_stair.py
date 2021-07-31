def countways(n):
    if n<=1:
        return 1
    return countways(n-1) + countways(n-2)
  
n = 4
print(countways(n))


