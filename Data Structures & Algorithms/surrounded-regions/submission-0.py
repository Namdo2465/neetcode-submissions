class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = set()
        directions = [[0,1], [1,0], [0,-1], [-1,0]]
        m = len(board)
        n = len(board[0])

        def bfs(row, col, board):
            visited.add((row, col))
            queue = deque([])
            queue.append((row, col))
            while queue:
                level_size = len(queue)
                for i in range(level_size):
                    x, y = queue.popleft()
                    for dir in directions:
                        x_dir = dir[0]
                        y_dir = dir[1]
                        new_row = x + x_dir
                        new_col = y + y_dir
                        if new_row in range(m) and new_col in range(n) and (new_row, new_col) not in visited and board[new_row][new_col] == "O":
                            visited.add((new_row, new_col))
                            queue.append((new_row, new_col))
        
        for row in range(m):
            for col in range(n):
                if board[row][col] == "O" and ((row == 0 or row == m - 1) or (col == 0 or col == n - 1)):
                    bfs(row, col, board)
        
        for row in range(m):
            for col in range(n):
                if board[row][col] == "O" and (row, col) not in visited:
                    board[row][col] = "X"

        