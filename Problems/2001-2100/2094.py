import itertools
from typing import List


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        uniqueNums = set()
        for perm in itertools.permutations(digits, 3):
            if perm[0] != 0 and perm[2] % 2 == 0:
                number = perm[0] * 100 + perm[1] * 10 + perm[2]
                uniqueNums.add(number)
        return sorted(uniqueNums)
