class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        squares = [set(), set(),set(),set(),set(),set(),set(),set(),set()]
        rows = [set(),set(),set(),set(),set(),set(),set(),set(),set()]
        cols = [set(), set(),set(),set(),set(),set(),set(),set(),set()]
        for i in range(9):
            for j in range(9):
                cur_element = board[i][j]
                print(f'current element: {cur_element}, row: {i}, col: {j}')
                if cur_element == '.':
                    continue
                cur_square = 3 * (i // 3) + (j // 3)
                if cur_element in rows[i]:
                    return False
                elif cur_element in cols[j]:
                    return False
                elif cur_element in squares[cur_square]:
                    return False
                rows[i].add(cur_element)
                cols[j].add(cur_element)
                squares[cur_square].add(cur_element)
        return True