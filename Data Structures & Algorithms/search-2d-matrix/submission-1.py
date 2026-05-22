class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        x = len(matrix)
        y = len(matrix[0])

        row_l = 0
        row_r = x - 1
        while row_l <= row_r:
            row_m = (row_l + row_r) // 2
            if matrix[row_m][0] > target:
                row_r = row_m - 1
            elif matrix[row_m][-1] < target:
                row_l = row_m + 1
            else:
                break

        if not(row_l <= row_r):
            return False
        row_m = (row_l + row_r) // 2
        index_l = 0
        index_r = y - 1
        while index_l <= index_r:
            index_m = (index_l + index_r) // 2
            if matrix[row_m][index_m] == target:
                return True
            elif matrix[row_m][index_m] > target:
                index_r = index_m - 1
            elif matrix[row_m][index_m] < target:
                index_l = index_m + 1
        return False