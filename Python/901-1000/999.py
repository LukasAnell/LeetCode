from typing import List


class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        rook = None
        for i in range(8):
            for j in range(8):
                if board[i][j] == "R":
                    rook = (i, j)
                    break
            if rook:
                break
        res = 0
        for i, j in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            x, y = rook
            while 0 <= x < 8 and 0 <= y < 8:
                if board[x][y] == "p":
                    res += 1
                    break
                if board[x][y] == "B":
                    break
                x += i
                y += j
        return res
