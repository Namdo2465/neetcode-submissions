class Solution:
    def list_is_valid(self, lst):
        used_set = set()
        for num in lst:
            if num != ".":
                if num in used_set:
                    return False
                else:
                    used_set.add(num)
        return True 
                
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        check_rows = True
        for row in board:
            check_rows = check_rows and self.list_is_valid(row)

        second_board = []        
        for i in range(9):
            columns = []
            for j in range(9):
                columns.append(board[j][i])
            second_board.append(columns)

        check_columns = True
        for row in second_board:
            check_columns = check_columns and self.list_is_valid(row) 


        third_board = []
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                third_board.append(board[i][j:j+3] + board[i+1][j:j+3] + board[i+2][j:j+3])
        check_squares = True      
        for row in third_board:
            check_squares = check_squares and self.list_is_valid(row) 


        res = check_rows and check_columns and check_squares
        return res
