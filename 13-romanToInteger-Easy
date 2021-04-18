class Solution:
    def romanToInt(self,s:str):
        conversion = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        sum = 0
        for i in range(len(s)-1):
            if conversion[s[i]] < conversion[s[i+1]]:
                sum -= conversion[s[i]]
            else:
                sum += conversion[s[i]]
        sum += conversion[s[-1]]
        return sum
