def process(word, i, j):
    if i >= j:
        return 0
        
    elif word[i] == word[j]:
        print("equal", word[i], word[j])
        return process(word, i+1, j-1)
        
    else:
        print("not equal",word[i], word[j])
        print(i,j)
        return (1+min(process(word,i+1,j), process(word,i,j-1)))
    

def main(word):
    return process(word,0,len(word)-1)

a = 'aaccpktrccaa'
print(main(a))


