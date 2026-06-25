class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        ROW = len(board)
        COL = len(board[0])

        seenRow = defaultdict(list)
        seenCol = defaultdict(list)
        seenGrid = defaultdict(list)

        for i in range(ROW):
            for j in range(COL):
                r = i//3
                c = j//3
                print(seenRow)
                print(seenCol)
                print(seenGrid)
                if board[i][j] != '.' and board[i][j] not in seenRow[i] and board[i][j] not in seenCol[j] and board[i][j] not in seenGrid[(r,c)]:
                    seenRow[i].append(board[i][j])
                    seenCol[j].append(board[i][j])
                    seenGrid[(r,c)].append(board[i][j])
                elif board[i][j] == '.':
                    continue
                else:
                    return False
        return True