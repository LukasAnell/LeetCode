class Solution:
    def kthCharacter(self, k: int) -> str:
        word = "a"
        while len(word) < k:
            newWord = "".join(
                chr((ord(c) - ord("a") + 1) % 26 + ord("a")) for c in word
            )
            word += newWord
        return word[k - 1]
