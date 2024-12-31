from typing import List


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        return [_ for _, num in enumerate(sorted(nums)) if num == target]
