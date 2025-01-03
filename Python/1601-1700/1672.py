from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max([sum(line) for line in accounts])
