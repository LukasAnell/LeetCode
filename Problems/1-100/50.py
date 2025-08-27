class Solution:
    def myPow(self, x: float, n: int) -> float:
        isNegative = n < 0
        if n == 0:
            return 1
        output = 1.0
        for _ in range(abs(n)):
            output *= x
        return 1 / output if isNegative else output
