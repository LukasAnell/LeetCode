from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        output = [[1]]
        for i in range(1, rowIndex + 1):
            output.append(
                [1]
                + [
                    output[i - 1][j] + output[i - 1][j + 1]
                    for j in range(len(output[i - 1]) - 1)
                ]
                + [1]
            )
        return output[rowIndex]
