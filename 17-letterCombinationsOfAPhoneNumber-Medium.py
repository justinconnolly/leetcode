class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if len(digits) < 1:
            return []
        numDict = {'2': 'abc',
                    '3': 'def',
                    '4': 'ghi',
                    '5': 'jkl',
                    '6': 'mno',
                    '7': 'pqrs',
                    '8': 'tuv',
                    '9': 'wxyz'}
        charList = []
        self.lcHelper(digits, numDict, 0, charList, "")
        return charList

    def lcHelper(self, digits, numDict, index, combinations, currWord):
        if len(currWord) == len(digits):
            combinations.append(currWord)
            return
        chars = numDict[digits[index]]
        for ch in chars:
            self.lcHelper(digits, numDict, index + 1, combinations, currWord + ch)

sol = Solution()
print(sol.letterCombinations('234'))