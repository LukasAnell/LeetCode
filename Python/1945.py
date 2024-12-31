class Solution:
    def getLucky(self, s: str, k: int) -> int:
        alphabetList = [ord(char) - ord('a') + 1 for char in s]
        addedDigits = str(sum([int(char) for char in ''.join(map(str, alphabetList))]))
        newSplit = [char for char in addedDigits]
        for _ in range(k - 1):
            addedDigits = str(sum([int(char) for char in newSplit]))
            newSplit = [char for char in addedDigits]
        return int(addedDigits)
