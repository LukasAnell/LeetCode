from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        newList = sorted(nums1 + nums2)
        lenNewList = len(newList)
        if lenNewList % 2 == 0:
            return (newList[lenNewList // 2 - 1] + newList[lenNewList // 2]) / 2
        else:
            return newList[lenNewList // 2]
