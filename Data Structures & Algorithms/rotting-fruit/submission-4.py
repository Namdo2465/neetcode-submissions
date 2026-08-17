class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()
        queue = deque([])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j))
                    visited.add((i, j))
        if len(queue) == 0:
            for i in range(rows):
                for j in range(cols):
                    if grid[i][j] == 1:
                        return -1
            return 0
        minutes = -1
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                cur_row, cur_col = queue.popleft()
                for dir_r, dir_c in directions:
                    new_row = cur_row + dir_r
                    new_col = cur_col + dir_c
                    if (
                        new_row in range(rows)
                        and new_col in range(cols)
                        and (new_row, new_col) not in visited
                        and grid[new_row][new_col] == 1
                    ):
                        queue.append((new_row, new_col))
                        visited.add((new_row, new_col))
                        grid[new_row][new_col] = -1
            minutes += 1
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1
        return minutes


# 2 1 1
# 1 1 1
# 0 1 2
