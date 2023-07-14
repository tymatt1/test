class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        array = [[1 for x in range(n)] for x in range(m)]

        for i in range (1, m):
            for j in range(1 , n):
                array[i][j] = array[i-1][j] + array[i][j-1]

        return array[-1][-1]