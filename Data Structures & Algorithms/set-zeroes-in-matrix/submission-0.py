class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zeroes = []
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zeroes.append([i,j])
        for pair in zeroes:
            row = pair[0]
            col = pair[1]
            for i in range(m):
                matrix[i][col] = 0
            for j in range(n):
                matrix[row][j] = 0
        

        