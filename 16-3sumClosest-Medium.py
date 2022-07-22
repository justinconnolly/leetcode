class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        min_diff = nums[0] + nums[1] + nums[2]
        nums.sort()
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if target == sum:
                    return target
                if abs(sum - target) < abs(min_diff - target):
                    min_diff = sum
                if target > sum:
                    left += 1
                else:
                    right -= 1
        return min_diff
