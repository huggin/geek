#Back-end complete function Template for Python 3
from collections import Counter

class Solution:
    def transform(self, A, B): 
        #code here.
        if len(A) != len(B):
            return -1
        
        c = Counter()
        for a in A:
            c[a] += 1
        for b in B:
            c[b] -= 1
            if c[b] < 0:
                return -1
        
        n = len(A)
        i = n-1
        j = n-1
        
        while i >= 0:
            if A[i] != B[j]:
                i -= 1
            else:
                i -= 1
                j -= 1
        
        return j + 1
        
        
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        line = input().strip().split()
        A = line[0]
        B = line[1]
        ob = Solution()
        print(ob.transform(A,B))
# } Driver Code Ends
