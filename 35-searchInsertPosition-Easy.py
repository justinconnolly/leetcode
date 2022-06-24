class Solution:
    # iterative solution
    def searchInsert(self, nums: list[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            index = (start + end) // 2
            if nums[index] > target:
                end = index - 1
            elif nums[index] < target:
                start = index + 1
            else:
                return index
        if target > nums[index]:
            return index + 1
        else: return index

    # recursive solution
    def searchInsert(self, nums: list[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        return self.siHelper(nums, start, end, target)       
        

    def siHelper(self, nums: list[int], start, end, target: int) -> int:
        if start < end:
            index = start + (end - start) // 2
            if target > nums[index]:
                return self.siHelper(nums, index + 1, end, target)
            elif target < nums[index]:
                return self.siHelper(nums, start, index, target)
            else:
                return index
        
        if nums[end] < target:
            return end + 1
        return start