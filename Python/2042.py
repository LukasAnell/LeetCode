class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        nums = [int(word) for word in s.split(" ") if word.isnumeric()]
        return all(x < y for x, y in zip(nums, nums[1:]))
