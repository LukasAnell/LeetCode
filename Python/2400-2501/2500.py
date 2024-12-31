from typing import List


class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        total = 0
        while any(grid):
            maxValues = []
            for row in grid:
                if row:
                    maxValues.append(max(row))
            for i in range(len(grid)):
                if grid[i]:
                    grid[i].remove(maxValues[i])
            total += max(maxValues)
            grid = [row for row in grid if row]
        return total
