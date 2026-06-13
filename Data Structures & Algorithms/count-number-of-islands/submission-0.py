class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        islands = 0
        visited = set()

        rows = len(grid)
        cols = len(grid[0])

        def bfs(r, c):
            q = collections.deque()
            visited.add((r,c))
            q.append((r,c))

            while q:
                row, col = q.popleft()
                directions = [[1,0], [-1,0], [0,1], [0,-1]]
                for dir_r, dir_c in directions:
                    if (row + dir_r in range(rows) and 
                    col + dir_c in range(cols) and 
                    grid[row + dir_r][col + dir_c] == "1" and 
                    (row + dir_r, col + dir_c) not in visited):
                        visited.add((row+dir_r, col+dir_c))
                        q.append((row+dir_r, col+dir_c))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1
        
        return islands


        