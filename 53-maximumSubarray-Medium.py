class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        dp = {}
        dp[0] = nums[0]
        max_sub = nums[0]
        for i in range(1, len(nums)):
            dp[i] = nums[i]
            if dp[i - 1] > 0:
                dp[i] += dp[i - 1]
            max_sub = max(max_sub, dp[i])
        return max_sub

sol = Solution()
print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))