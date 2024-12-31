class Solution:
    def isThree(self, n: int) -> bool:
        numDivisors = 2
        for i in range(2, n):
            if n % i == 0:
                numDivisors += 1
            if numDivisors > 3:
                return False
        return numDivisors == 3
