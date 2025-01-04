from typing import List


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(len(nums)):
            answer += [abs(sum(nums[:i]) - sum(nums[i + 1 :]))]
        return answer
