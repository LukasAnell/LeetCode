from collections import Counter
from typing import List


class Solution:
    def twoOutOfThree(
        self, nums1: List[int], nums2: List[int], nums3: List[int]
    ) -> List[int]:
        count = Counter(set(nums1) | set(nums2) | set(nums3))
        return [
            num
            for num in count
            if (num in nums1 and num in nums2)
            or (num in nums1 and num in nums3)
            or (num in nums2 and num in nums3)
        ]
