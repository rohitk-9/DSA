#Basic
'''You are given a string s. You need to reverse the string.

Example 1:

Input:
s = Geeks
Output: skeeG

Example 2:

Input:
s = for
Output: rof'''

class Solution:
    def reverseWord(self, s):
        return s[::-1]
    
obj = Solution()
s = "for"
print(obj.reverseWord(s))