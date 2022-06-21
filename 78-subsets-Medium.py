class Solution:
    def Xsubsets(self, nums: list[int]) -> list[list[int]]:
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

    def subsets(self, nums: list[int]) -> list[list[int]]:
        length = len(nums)
        powerSet = []
        for i in range(2**length):
            subset = []
            index = length - 1
            while i:
                if i & 1:
                    subset.append(nums[index])
                index -= 1
                i >>= 1
            powerSet.append(subset)
        return powerSet