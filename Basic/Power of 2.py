#Basic
'''Given a non-negative integer N. The task is to check if N is a power of 2. More formally, check if N can be expressed as 2x for some integer x. Return true if N is power of 2 else return false.

Example 1:

Input: 
N = 8
Output: 
YES
Explanation:
8 is equal to 2 raised to 3 (23 = 8).

Example 2:

Input: 
N = 98
Output: 
NO
Explanation: 
98 cannot be obtained by any power of 2.'''

class Solution:
    def isPowerofTwo(self,n):
        if n <= 0:
            return False
        return n & (n - 1) == 0
    
obj = Solution()
print(obj.isPowerofTwo(98))
    


