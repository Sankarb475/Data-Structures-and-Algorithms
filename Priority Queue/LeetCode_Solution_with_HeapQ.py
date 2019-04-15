# solution of :: https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/ 

#1 solution 

import heapq
class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        heapq.heapify(A)
        for i in range(K):
            heapq.heapreplace(A,-A[0])
        return sum(A)
        
        
#2 solution

class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        A.sort()
        B = [abs(num) for num in A]
        count_neg_number = 0
        # getting the number of negative number present
        for i in A:
            if i >= 0:
                break
            count_neg_number += 1
        # if negative numbers are more than the value of K, then K smallest negative numbers will be changed to positive

        if K <= count_neg_number:
            chunk1 = sum([abs(num) for num in A[0:K]]) # K negative numbers are converted to poistive
            chunk2 = sum(A[K:])
            return chunk1 + chunk2
        else:
            if (K - count_neg_number) % 2 == 0:
                return sum(B)
            else:
                return sum(B) - 2 * min(B)
                
 
        
