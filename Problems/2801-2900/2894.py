class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        sumNums = 0
        for i in range(n + 1):
            if i % m == 0:
                sumNums -= i
            else:
                sumNums += i
        return sumNums
