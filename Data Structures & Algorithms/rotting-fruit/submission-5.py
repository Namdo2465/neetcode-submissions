from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        queue = deque([])
        visited = set()
        fresh_fruits = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                    visited.add((r, c))
                elif grid[r][c] == 1:
                    fresh_fruits += 1
        
        if fresh_fruits == 0:
            return 0

        minutes = -1

        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                r, c = queue.popleft()
                if grid[r][c] == 1:
                    fresh_fruits -= 1
                for dir_r, dir_c in directions:
                    new_r, new_c = r + dir_r, c + dir_c
                    if (
                        0 <= new_r < rows
                        and 0 <= new_c < cols
                        and (new_r, new_c) not in visited
                        and grid[new_r][new_c] == 1
                    ):
                        queue.append((new_r, new_c))
                        visited.add((new_r, new_c))
            minutes += 1
        
        if fresh_fruits > 0:
            return -1
        return minutes

        

