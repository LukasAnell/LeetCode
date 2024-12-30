from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        output = [[1]]
        for i in range(1, numRows):
            output.append(
                [1]
                + [
                    output[i - 1][j] + output[i - 1][j + 1]
                    for j in range(len(output[i - 1]) - 1)
                ]
                + [1]
            )
        return output
