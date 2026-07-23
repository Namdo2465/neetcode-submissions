class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        seen = set()
        m = len(matrix)
        n = len(matrix[0])
        x_dir = 0
        y_dir = 1
        x, y = 0, 0
        res = []
        while len(res) != m*n:
            if (x,y) not in seen and x in range(m) and y in range(n):
                res.append(matrix[x][y])
                seen.add((x,y))
                x += x_dir
                y += y_dir
            else:
                x -= x_dir
                y -= y_dir
                x_dir, y_dir = y_dir * 1, x_dir * (-1)
                x += x_dir
                y += y_dir
        return res

