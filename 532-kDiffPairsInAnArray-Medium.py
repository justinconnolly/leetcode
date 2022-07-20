class Solution:
    def findPairs(self, nums: list[int], k: int) -> int:
        pairs = 0
        dict = {}
        for i, v in enumerate(nums):
            if v in dict:
                if k == 0 and dict[v] == 1:
                    pairs += 1
                dict[v] += 1
            else:
                if v - k in dict:
                    pairs += 1
                if v + k in dict:
                    pairs += 1
                dict[v] = 1
        return pairs
if __name__ == "__main__":
    arrs = [[3,1,4,1,5],
            [1,2,3,4,5]]
    diffs = [2,1]
    answers = [2,4]
    sol = Solution()
    for i,v in enumerate(arrs):
        print(f"Checking {v}")
        assert answers[i] == sol.findPairs(v, diffs[i])