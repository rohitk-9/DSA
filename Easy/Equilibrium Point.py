#Easy
'''Given an array A of n non negative numbers. The task is to find the first equilibrium point in an array. Equilibrium point in an array is an index (or position) such that the sum of all elements before that index is same as sum of elements after it.

Note: Return equilibrium point in 1-based indexing. Return -1 if no such point exists. 

Example 1:

Input: 
n = 5 
A[] = {1,3,5,2,2} 
Output: 
3 
Explanation:  
equilibrium point is at position 3 as sum of elements before it (1+3) = sum of elements after it (2+2). 

Example 2:

Input:
n = 1
A[] = {1}
Output: 
1
Explanation:
Since there's only element hence its only the equilibrium point.'''


class Solution:

    def equilibriumPoint(self,arr, n):
        sum1=0
        if n==1:
            return(n)
        for i in range(2,n):
            sum1 += arr[i]
        sum2 = arr[0]
        ptr = arr[1]
        for i in range(2,n):
            if sum1 == sum2:
                return(i)
                break
            else:
                sum2 += ptr
                ptr = arr[i]
                sum1 -=ptr
        return -1
    

obj = Solution()
arr = [1,3,5,2,2]
print(obj.equilibriumPoint(arr, len(arr)))
