class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowL = 0
        rowR = len(matrix) - 1


        colL = 0
        colR = len(matrix[0]) - 1
        
        #First find which row
        while rowL <= rowR:
            middle = (rowL + rowR) // 2
            row = middle
            if target > matrix[middle][colR]:
                rowL = middle + 1
            elif target < matrix[middle][colL]:
                rowR = middle - 1
            else:
                break

        if not (rowL <= rowR):
            return False

        #Then find which col
        while colL <= colR:
            middle = (colL + colR )// 2

            if target > matrix[row][middle]:
                colL = middle + 1
            elif target < matrix[row][middle]:
                colR = middle - 1
            else:
                return True
        return False