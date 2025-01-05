from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        numsLen = len(nums)
        closest = float("inf")
        for i in range(numsLen):
            left, right = i + 1, numsLen - 1
            while left < right:
                currentSum = nums[i] + nums[left] + nums[right]
                if abs(currentSum - target) < abs(closest - target):
                    closest = currentSum
                if currentSum < target:
                    left += 1
                elif currentSum > target:
                    right -= 1
                else:
                    return closest
        return closest
