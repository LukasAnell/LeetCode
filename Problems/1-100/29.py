class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        isNegative = (dividend < 0) != (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0
        while dividend >= divisor:
            temp = divisor
            multiple = 1
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            dividend -= temp
            quotient += multiple
        if isNegative:
            quotient = -quotient
        return min(max(quotient, -(2**31)), 2**31 - 1)
