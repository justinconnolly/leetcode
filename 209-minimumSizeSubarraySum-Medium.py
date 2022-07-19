class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        curr_sum = 0
        start = 0
        length = len(nums) + 1
        for i,v in enumerate(nums):
            curr_sum += v
            while curr_sum >= target:
                length = min(length, i - start + 1)
                curr_sum -= nums[start]
                start += 1
        if length == len(nums) + 1:
            return 0
        return length