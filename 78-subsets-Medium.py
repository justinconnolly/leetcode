class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        length = len(nums)
        powerSet = []
        for i in range( 2**length):
            for index in range(length):
                subset = []
                for pos in range(length):
                    if (i >> pos) & 1:
                        subset.append(nums[pos])
            powerSet.append(subset)
        return powerSet