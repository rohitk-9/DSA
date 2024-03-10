'''Given an unsorted array A of size N that contains only non negative integers, find a continuous sub-array that adds to a given number S and return the left and right index(1-based indexing) of that subarray.

In case of multiple subarrays, return the subarray indexes which come first on moving from left to right.

Note:- You have to return an ArrayList consisting of two elements left and right. In case no such subarray exists return an array consisting of element -1.

Example 1:

Input:
N = 5, S = 12
A[] = {1,2,3,7,5}
Output: 2 4
Explanation: The sum of elements 
from 2nd position to 4th position 
is 12.

Example 2:

Input:
N = 10, S = 15
A[] = {1,2,3,4,5,6,7,8,9,10}
Output: 1 5
Explanation: The sum of elements 
from 1st position to 5th position
is 15.
'''

#User function Template for python3

#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self,arr, n, s): 
        start = 0 
        end = 0
        sub_sum = 0
        flag = False
        res = []
        while end < n:
            sub_sum += arr[end]
            while sub_sum > s and start < end:
                sub_sum = sub_sum - arr[start]
                start += 1 
            if sub_sum == s:
                flag = True
                res = [start+1,end+1]
                break
            end += 1 
        if flag :       
            return res  
        else:
            return [-1]

