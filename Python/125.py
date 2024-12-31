class Solution:
    def isPalindrome(self, s: str) -> bool:
        together = [char.lower() for char in s if char.isalnum()]
        return together == together[::-1]
