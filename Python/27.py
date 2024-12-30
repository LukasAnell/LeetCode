from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        newNums = list()
        for num in nums:
            if num != val:
                newNums.append(num)
        for i in range(len(newNums)):
            nums[i] = newNums[i]
        return len(newNums)
