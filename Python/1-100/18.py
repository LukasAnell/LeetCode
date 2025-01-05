from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        numsLen = len(nums)
        result = []
        for i in range(numsLen):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, numsLen):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                left, right = j + 1, numsLen - 1
                while left < right:
                    currentSum = nums[i] + nums[j] + nums[left] + nums[right]
                    if currentSum < target:
                        left += 1
                    elif currentSum > target:
                        right -= 1
                    else:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
        return result
