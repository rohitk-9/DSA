#easy
'''Given an array Arr of size N, print the second largest distinct element from an array. If the second largest element doesn't exist then return -1.

Example 1:

Input: 
N = 6
Arr[] = {12, 35, 1, 10, 34, 1}
Output: 34
Explanation: The largest element of the 
array is 35 and the second largest element
is 34.

Example 2:

Input: 
N = 3
Arr[] = {10, 5, 10}
Output: 5
Explanation: The largest element of 
the array is 10 and the second 
largest element is 5.'''

#User function Template for python3
class Solution:

    def print2largest(self,arr, n):
        value_to_remove = max(arr)
        my_list = [x for x in arr if x != value_to_remove]
        if len(my_list)==0:
            return -1
        return max(my_list)

