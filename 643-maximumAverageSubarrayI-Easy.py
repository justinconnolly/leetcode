class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        sum = 0
        max_av = 0
        for i, v in enumerate(nums):
            sum += v
            if i < k:
                max_av = sum
            else:
                sum -= nums[i - k]
                max_av = max(max_av, sum)
        return max_av / k