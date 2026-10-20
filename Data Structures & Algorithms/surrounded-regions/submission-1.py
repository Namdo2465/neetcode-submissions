from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        visited = set()
        queue = deque([])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for r in range(rows):
            if board[r][0] == 'O':
                queue.append((r, 0))
                visited.add((r, 0))
            if board[r][cols - 1] == 'O':
                queue.append((r, cols - 1))
                visited.add((r, cols - 1))
        
        for c in range(cols):
            if board[0][c] == 'O':
                queue.append((0, c))
                visited.add((0, c))
            if board[rows - 1][c] == 'O':
                queue.append((rows - 1, c))
                visited.add((rows - 1, c))
        
        while queue:
            r, c = queue.popleft()
            for dir_r, dir_c in directions:
                new_r, new_c = r + dir_r, c + dir_c
                if (
                    0 <= new_r < rows
                    and 0 <= new_c < cols
                    and (new_r, new_c) not in visited
                    and board[new_r][new_c] == 'O'
                ):
                    visited.add((new_r, new_c))
                    queue.append((new_r, new_c))
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and (r, c) not in visited:
                    board[r][c] = 'X'
