from typing import List

class Solution:
    @staticmethod
    def sortColors(nums: List[int]) -> None:
        for limit in range(len(nums) - 1, 0, -1):
            for i in range(limit):
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
