class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        self.mergeSort(nums, k)
        return nums[-k]
        
    def mergeSort(self, nums, k):

        if len(nums) <= 1:
            if nums[0] < k:
                return []
            return nums
        firstHalf = nums[:len(nums)//2]
        secondHalf = nums[len(nums)//2:]
        self.mergeSort(firstHalf, k)
        self.mergeSort(secondHalf, k)
        firstCounter = 0
        secondCounter = 0
        for index, value in enumerate(nums):

            if firstCounter == len(firstHalf):
                nums[index] = secondHalf[secondCounter]
                secondCounter += 1
            elif secondCounter == len(secondHalf):
                nums[index] = firstHalf[firstCounter]
                firstCounter += 1
            elif firstHalf[firstCounter] <= secondHalf[secondCounter]:
                nums[index] = firstHalf[firstCounter]
                firstCounter += 1
            else:
                nums[index] = secondHalf[secondCounter]
                secondCounter += 1

class Solution2:
    def __init__(self):
        from random import randint
    def findKthLargest(self, nums: list[int], k: int) -> int:
        self.quickSort(nums,0,len(nums))
        return nums[-k]
        
    def quickSort(self,myList: list, start: int, end: int):
        if end <= 1:
            return

        pivot = myList[start + randint(0,end - 1)]
        p = start - 1
        j = start
        q = start + end

        while j < q:
            if myList[j] < pivot:
                p += 1
                temp = myList[j]
                myList[j] = myList[p]
                myList[p] = temp
                j += 1
            elif myList[j] > pivot:
                q -= 1
                temp = myList[j]
                myList[j] = myList[q]
                myList[q] = temp
            else:
                j += 1

        self.quickSort(myList, start, p - start + 1)
        self.quickSort(myList, q, end - (q - start))

sol = Solution()
myList = [1,2,3,4,5]
k = 2
print(sol.findKthLargest(myList, k))