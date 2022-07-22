class Solution:
    # naive
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for item in nums:
            for item2 in nums[item:]:
                if item + item2 == target:
                    return [item, item2]
    
    # O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i,v in enumerate(nums):
            if target - v in dict:
                return [i, dict[target - v]]
            dict[v] = i