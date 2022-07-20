class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        sum = 0
        max_av = 0
        for i, v in enumerate(nums):
            if i < k:
                sum += v
                max_av = sum
            else:
                sum += v - nums[i - k]
                max_av = max(max_av, sum)
        return max_av / k