https://www.geeksforgeeks.org/longest-common-substring-dp-29/?ref=leftbar-rightbar

def lcs(i, j, count):
 
    if (i == 0 or j == 0):
        return count
 
    if (X[i - 1] == Y[j - 1]):
        count = lcs(i - 1, j - 1, count + 1)
 
    count = max(count, max(lcs(i, j - 1, 0),
                           lcs(i - 1, j, 0)))
 
    return count
 
 
# Driver code
if __name__ == "__main__":
 
    X = "abcdxyz"
    Y = "xyzabcdxyz"
    n = len(X)
    m = len(Y)
 
    print(lcs(n, m, 0))
 
# scope of X and Y are beyond main function
