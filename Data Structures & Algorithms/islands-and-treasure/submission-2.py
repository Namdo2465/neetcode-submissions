from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        rows, cols = len(grid), len(grid[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        queue = deque([])
        visited = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))
                    visited.add((r, c))

        dist = 1
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                r, c = queue.popleft()
                for dir_r, dir_c in directions:
                    new_r, new_c = r + dir_r, c + dir_c
                    if (
                        0 <= new_r < rows and
                        0 <= new_c < cols and
                        (new_r, new_c) not in visited and
                        grid[new_r][new_c] == INF
                    ):
                        queue.append((new_r, new_c))
                        visited.add((new_r, new_c))
                        grid[new_r][new_c] = dist
            dist += 1
        