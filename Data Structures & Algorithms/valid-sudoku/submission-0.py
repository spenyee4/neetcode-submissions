class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        ROW = len(board)
        COL = len(board[0])

        print(ROW)
        print(COL)

        rowTable = defaultdict(list)
        colTable = defaultdict(list)
        gridTable = defaultdict(list)

        for i in range(ROW):
            for j in range(COL):
                square_row = i//3
                square_col = j//3
                if board[i][j] in rowTable[i] or board[i][j] in colTable[j] or board[i][j] in gridTable[(square_row,square_col)]:
                    return False
                if board[i][j] == '.':
                    continue
                rowTable[i].append(board[i][j]) 
                colTable[j].append(board[i][j]) 
                gridTable[(square_row,square_col)].append(board[i][j]) 

        
        return True