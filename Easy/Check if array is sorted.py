#easy
'''Given an array arr[] of size N, check if it is sorted in non-decreasing order or not. 

Example 1:

Input:
N = 5
arr[] = {10, 20, 30, 40, 50}
Output: 1
Explanation: The given array is sorted.

Example 2:

Input:
N = 6
arr[] = {90, 80, 100, 70, 40, 30}
Output: 0
Explanation: The given array is not sorted.'''

#User function Template for python3

class Solution:
    def arraySortedOrNot(self, arr, n):
        my_list = [x for x in arr]
        arr.sort()
        if my_list==arr:
            return 1
        else:
            return 0


