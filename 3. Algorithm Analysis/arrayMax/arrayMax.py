class Solution(object):
    def arrayMax(A,n):
        currentMax = A[0]
        for i in range(1,n):
            if currentMax < A[i]:
                currentMax = A[i]
        return currentMax
