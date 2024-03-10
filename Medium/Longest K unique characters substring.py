'''Given a string you need to print the size of the longest possible substring that has exactly K unique characters. If there is no possible substring then print -1.

Example 1:

Input:
S = "aabacbebebe", K = 3
Output: 
7
Explanation: 
"cbebebe" is the longest substring with 3 distinct characters.

Example 2:

Input: 
S = "aaaa", K = 2
Output: -1
Explanation: 
There's no substring with 2 distinct characters.
'''


class Solution:

    def longestKSubstr(self, s, k):
        m = {}
        for x in s:
            m[x] = 0
        
        uniq = 0
        i = 0
        j = 0
        res = 0
        n = len(s)
        
        while j < n:
            while j < n:
                if m[s[j]] == 0:
                    uniq += 1
                m[s[j]] += 1

                if uniq > k:
                    break
                j += 1
        
            if uniq >= k:
                res = max(res, j-i)
            
            if j == n:
                break

            while i < n:
                if m[s[i]] == 1:
                    uniq -= 1
                m[s[i]] -= 1

                if uniq == k:
                    break
                i += 1
        
            i += 1
            j += 1
        
        if res == 0:
            return -1
        return res
