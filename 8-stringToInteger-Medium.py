class Solution:
    def myAtoi(self, s: str) -> int:
        numSet = {'1','2','3', '4','5','6','7','8','9','0'}
        sign = 1
        pos = 0
        signed = False
        leading = False
        if len(s) <= 1:
            if s in numSet:
                return int(s)
            return 0
        while s[pos] == ' ' or s[pos] == '0':
            if s[pos] == '0':
                leading = True
            pos += 1
            if pos >= len(s):
                return 0
            if s[pos] == ' ' and leading:
                return 0
        if s[pos] == '-':
            if leading:
                return 0
            sign = -1
            pos += 1
            signed = True
        elif s[pos] == '+':
            if leading:
                return 0
            if signed:
                return 0
            pos += 1
        if s[pos] not in numSet:
            return 0
        while s[pos] == '0':
            pos += 1
        intStart = pos
        intEnd = intStart

        while intEnd < len(s):
            if s[intEnd] in numSet:
                intEnd += 1
                if intEnd - intStart > 9:
                    if int(s[intStart:intEnd]) >= (2**31 - 1):
                        if sign > 0:
                            return (2**31) - 1
                        elif int(s[intStart:intEnd]) >= (2**31):
                            return -(2**31)
            else:
                break
        if intEnd - intStart < 1:
            return 0
        return sign * int(s[intStart:intEnd])