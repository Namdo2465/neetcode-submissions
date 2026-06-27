class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        max_area = 0

        def bfs(r,c):
            nonlocal max_area
            area = 1
            queue = collections.deque()
            visited.add((r,c))
            queue.append((r,c))
            while queue:
                row, col = queue.popleft()
                directions = [[1,0], [-1,0], [0,1], [0,-1]]
                for direct in directions:
                    x, y = direct[0], direct[1]
                    if row + x in range(rows) and col + y in range(cols) and grid[row+x][col+y] == 1 and (row+x, col+y) not in visited:
                        area += 1
                        visited.add((row+x, col+y))
                        queue.append((row+x, col+y))
            max_area = max(max_area, area)
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c] == 1:
                    bfs(r,c)
        return max_area
