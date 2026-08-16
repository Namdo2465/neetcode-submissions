class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        cnt = [[0 for _ in row] for row in heights]
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        def atlantic_bfs(r, c):
            atlantic_visited = set()
            atlantic_visited.add((r, c))
            queue = deque([])
            queue.append((r,c))
            while queue:
                current_row, current_col = queue.popleft()
                if current_row == rows - 1 or current_col == cols - 1:
                    cnt[r][c] += 1
                    break
                for dir_r, dir_c in directions:
                    new_row = current_row + dir_r
                    new_col = current_col + dir_c
                    if (
                        new_row in range(rows) 
                        and new_col in range(cols) 
                        and (new_row, new_col) not in atlantic_visited 
                        and heights[new_row][new_col] <= heights[current_row][current_col]
                    ):
                        queue.append((new_row, new_col))
                        atlantic_visited.add((new_row, new_col))
        def pacific_bfs(r, c):
            pacific_visited = set()
            pacific_visited.add((r, c))
            queue = deque([])
            queue.append((r,c))
            while queue:
                current_row, current_col = queue.popleft()
                if current_row == 0 or current_col == 0:
                    cnt[r][c] += 1
                    break
                for dir_r, dir_c in directions:
                    new_row = current_row + dir_r
                    new_col = current_col + dir_c
                    if (
                        new_row in range(rows) 
                        and new_col in range(cols) 
                        and (new_row, new_col) not in pacific_visited 
                        and heights[new_row][new_col] <= heights[current_row][current_col]
                    ):
                        queue.append((new_row, new_col))
                        pacific_visited.add((new_row, new_col))
        for i in range(rows):
            for j in range(cols):
                atlantic_bfs(i, j)
                pacific_bfs(i, j)
        res = []
        for i in range(rows):
            for j in range(cols):
                if cnt[i][j] == 2:
                    res.append([i,j])

        return res




        