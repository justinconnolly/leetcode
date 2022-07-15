class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        if len(nums) <= 1:
            return 0
        nums.sort()
        median = nums[len(nums) // 2]
        sum = 0
        for num in nums:
            sum += abs(round(median - num))
        return sum