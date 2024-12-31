class Solution:
    def minTimeToType(self, word: str) -> int:
        time = 0
        pointer = 'a'
        for char in word:
            clockwise = (ord(char) - ord(pointer)) % 26
            counterClockwise = (ord(pointer) - ord(char)) % 26
            time += min(clockwise, counterClockwise) + 1
            pointer = char
        return time
