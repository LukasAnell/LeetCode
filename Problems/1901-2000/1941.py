class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counts = [s.count(x) for x in set(s)]
        return len(set(counts)) == 1
