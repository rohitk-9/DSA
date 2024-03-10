#easy
'''Given two sorted arrays arr and brr and a number x, find the pair whose sum is closest to x and the pair has an element from each array. In the case of multiple closest pairs return any one of them.
Note: Can return the two numbers in any manner. The driver code takes care of the printing of the closest difference.

Example 1:

Input : N = 4, M = 4
arr[ ] = {1, 4, 5, 7}
brr[ ] = {10, 20, 30, 40} 
X = 32
Output : 
1, 30
Explanation:
The closest pair whose sum is closest
to 32 is {1, 30} = 31.

Example 2:

Input : N = 4, M = 4
arr[ ] = {1, 4, 5, 7}
brr[ ] = {10, 20, 30, 40}
X = 50 
Output : 
7, 40 
Explanation: 
The closest pair whose sum is closest
to 50 is {7, 40} = 47.'''

#User function Template for python3

class Solution:
    def printClosest (self,arr, brr, n, m, x) : 
        diff = float('inf')
        res1=0
        res2=0
        i=0
        j=m-1
        while(i<n and j>=0):
            sum = arr[i] + brr[j]
            c_diff = abs(sum-x)
            if (c_diff<diff):
                diff = c_diff
                res1 = arr[i]
                res2 = brr[j]
            if sum>x:
                j-=1
            else:
                i+=1
        return res1, res2

