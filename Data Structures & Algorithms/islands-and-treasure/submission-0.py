class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])

        INF = 2147483647
        directions = [[0,1], [0,-1], [1,0], [-1,0]]

        def bfs(grid, x, y):
            dist = 0
            visited = set()
            visited.add((x,y))
            queue = collections.deque([(x, y)])
            while queue:
                level_size = len(queue)
                for i in range(level_size):
                    x, y = queue.popleft()
                    if grid[x][y] == 0:
                        return dist
                    for dir in directions:
                        x_move = dir[0]
                        y_move = dir[1]
                        new_x = x + x_move
                        new_y = y + y_move
                        if (new_x in range(rows) and 
                        new_y in range(cols) and 
                        (new_x, new_y) not in visited and 
                        grid[new_x][new_y] != -1):
                            queue.append((new_x, new_y))
                            visited.add((new_x, new_y))
                dist += 1
            return INF

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == INF:
                    grid[row][col] = bfs(grid, row, col)



                        

            
