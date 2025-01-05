from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        letterMapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        output = []
        for char in digits:
            if not output:
                output = list(letterMapping[char])
            else:
                output = [i + j for i in output for j in letterMapping[char]]
        return output
