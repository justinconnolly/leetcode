#two pointers
#one moves forward every iteration
#one stops if List[i] == val
#at every iteration, lag[i] = lead[i]

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        lag = 0
        for lead,value in enumerate(nums):
            nums[lag] = nums[lead]
            if value != val:
                lag += 1
        return lag
