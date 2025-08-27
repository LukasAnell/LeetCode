from typing import List


class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        count = 0
        length = len(nums)
        for i in range(length):
            for j in range(i + 1, length):
                for k in range(j + 1, length):
                    for l in range(k + 1, length):
                        if nums[i] + nums[j] + nums[k] == nums[l]:
                            count += 1
        return count
