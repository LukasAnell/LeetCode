from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxAmount = 0
        left, right = 0, len(height) - 1
        while left < right:
            maxAmount = max(
                maxAmount, min(height[left], height[right]) * (right - left)
            )
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxAmount
