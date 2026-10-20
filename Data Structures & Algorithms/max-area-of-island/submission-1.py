class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        visited = set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if (r, c) in visited:
                return 0
            area = 1
            visited.add((r, c))
            for dir_r, dir_c in directions:
                new_r, new_c = r + dir_r, c + dir_c
                if (
                    0 <= new_r < rows
                    and 0 <= new_c < cols
                    and (new_r, new_c) not in visited
                    and grid[new_r][new_c] == 1   
                ):
                    area += dfs(new_r, new_c)
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))

        return max_area
                





        