class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        pacific_visited = set()
        def pacific_bfs(r, c):
            queue = deque([])
            queue.append((r, c))
            pacific_visited.add((r, c))
            while queue:
                current_row, current_col = queue.popleft()
                for dir_r, dir_c in directions:
                    new_row = current_row + dir_r
                    new_col = current_col + dir_c
                    if (
                        new_row in range(rows) 
                        and new_col in range(cols)
                        and (new_row, new_col) not in pacific_visited
                        and heights[new_row][new_col] >= heights[current_row][current_col]
                    ):
                        queue.append((new_row, new_col))
                        pacific_visited.add((new_row, new_col))

        atlantic_visited = set()
        def atlantic_bfs(r, c):
            queue = deque([])
            queue.append((r, c))
            atlantic_visited.add((r, c))
            while queue:
                current_row, current_col = queue.popleft()
                for dir_r, dir_c in directions:
                    new_row = current_row + dir_r
                    new_col = current_col + dir_c
                    if (
                        new_row in range(rows) 
                        and new_col in range(cols)
                        and (new_row, new_col) not in atlantic_visited
                        and heights[new_row][new_col] >= heights[current_row][current_col]
                    ):
                        queue.append((new_row, new_col))
                        atlantic_visited.add((new_row, new_col))

        
        for i in range(rows):
            pacific_bfs(i, 0)
            atlantic_bfs(i, cols - 1)
        for j in range(cols):
            pacific_bfs(0, j)
            atlantic_bfs(rows - 1, j)
        res = []
        for (row, col) in pacific_visited:
            if (row, col) in atlantic_visited:
                res.append([row, col])
        return res



        