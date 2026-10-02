class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()
        def dfs(r, c, i):
            if (r, c) in visited:
                return False
            visited.add((r, c))
            if i == len(word):
                return True
            for dir_r, dir_c in directions:
                new_r, new_c = r + dir_r, c + dir_c
                if (
                    new_r in range(rows)
                    and new_c in range(cols)
                    and (new_r, new_c) not in visited
                    and board[new_r][new_c] == word[i]
                ):
                    if dfs(new_r, new_c, i + 1):
                        return True
            visited.remove((r, c))
            return False

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if len(word) == 1:
                        return True
                    elif dfs(r, c, 1):
                        return True
        return False
            
                
