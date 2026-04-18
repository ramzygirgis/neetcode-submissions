class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set(), set(), set(), set(), set(), set(), set(), set(), set()]
        cols = [set(), set(), set(), set(), set(), set(), set(), set(), set()]
        sqrs = [set(), set(), set(), set(), set(), set(), set(), set(), set()]
        for i in range(9):
            for j in range(9):
                x = board[i][j]
                if x == ".":
                    continue
                if x in rows[i] or x in cols[j] or x in sqrs[3 * (i // 3) + j // 3]:
                    return False
                rows[i].add(x)
                cols[j].add(x)
                sqrs[3 * (i // 3) + j // 3].add(x)
        return True