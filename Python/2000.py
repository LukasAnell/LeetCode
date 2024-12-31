class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        index = word.find(ch) + 1
        return word[:index][::-1] + word[index:]
