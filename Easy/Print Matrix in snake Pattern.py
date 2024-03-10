#Easy
'''Given a matrix of size N x N. Print the elements of the matrix in the snake like pattern depicted below.

Example 1:

Input:
N = 3 
matrix[][] = {{45, 48, 54},
             {21, 89, 87}
             {70, 78, 15}}
Output: 
45 48 54 87 89 21 70 78 15 
Explanation:
Matrix is as below:
45 48 54
21 89 87
70 78 15
Printing it in snake pattern will lead to 
the output as 45 48 54 87 89 21 70 78 15.

Example 2:

Input:
N = 2
matrix[][] = {{1, 2},
              {3, 4}}
Output: 
1 2 4 3
Explanation:
Matrix is as below:
1 2 
3 4
Printing it in snake pattern will 
give output as 1 2 4 3.'''



class Solution:
    def snakePattern(self, matrix): 
        n = len(matrix)
        self.ans_list = []
        m = n
        for i in range(n):
            if i%2==0:
                for j in range(n):
                    self.ans_list.append(matrix[i][j])
            else:
                for k in range(m-1, -1, -1):
                    self.ans_list.append(matrix[i][k])
        return self.ans_list

obj = Solution()
matrix = [[45, 48, 54],
          [21, 89, 87],
          [70, 78, 15]]
print(obj.snakePattern(matrix))