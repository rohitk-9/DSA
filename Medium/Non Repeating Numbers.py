'''Given an array A containing 2*N+2 positive numbers, out of which 2*N numbers exist in pairs whereas the other two number occur exactly once and are distinct. Find the other two numbers. Return in increasing order.

Example 1:

Input: 
N = 2
arr[] = {1, 2, 3, 2, 1, 4}
Output:
3 4 
Explanation:
3 and 4 occur exactly once.

Example 2:

Input:
N = 1
arr[] = {2, 1, 3, 2}
Output:
1 3
Explanation:
1 3 occur exactly once.'''

#User function Template for python3

class Solution:
    def singleNumber(self, nums):
        d = {}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        single=[]
        for j in d.keys():
            if d[j]==1:
                single.append(j)
        single.sort()
        return(single)


