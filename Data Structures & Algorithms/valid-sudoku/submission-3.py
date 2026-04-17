class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[],[],[],[],[],[],[],[],[]]
        cols = [[],[],[],[],[],[],[],[],[]]
        squares = [[],[],[],[],[],[],[],[],[]]
        for i in range(9):
            for j in range(9):
                cur = board[i][j]
                if cur == '.':
                    continue
                if cur in rows[i]:
                    return False
                if cur in cols[j]:
                    return False
                if cur in squares[3*(i//3) +(j//3)]:
                    return False

                rows[i].append(cur)
                cols[j].append(cur)
                squares[3*(i//3) +(j//3)].append(cur)
                
        return True