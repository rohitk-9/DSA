#easy
'''Given an array a of size N which contains elements from 0 to N-1, you need to find all the elements occurring more than once in the given array. Return the answer in ascending order. If no such element is found, return list containing [-1]. 

Note: The extra space is only for the array to be returned. Try and perform all operations within the provided array. 

Example 1:

Input:
N = 4
a[] = {0,3,1,2}
Output: 
-1
Explanation: 
There is no repeating element in the array. Therefore output is -1.

Example 2:

Input:
N = 5
a[] = {2,3,1,2,3}
Output: 
2 3 
Explanation: 
2 and 3 occur more than once in the given array.'''

class Solution:
    def duplicates(self, arr, n): 
        d = {}
        res = []
        for i in arr:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        
        sorted_dict = dict(sorted(d.items(), key=lambda item: item[1]))
        
        for key in sorted_dict.keys():
            if sorted_dict[key] > 1:
                res.append(key)
        
        if not res:
            return [-1]
        return sorted(res)

            

