class Solution:
    def myAtoi(self, s: str) -> int:
        numSet = {'1','2','3', '4','5','6','7','8','9','0'}
        sign = 1
        pos = 0
        leading = False
        length = len(s)
        if length <= 1:
            if s in numSet:
                return int(s)
            return 0
        if s[pos] == '0':
            leading = True
            while s[pos] == '0':
                pos += 1
                if pos >= length:
                    return 0
        while s[pos] == ' ':
            if leading:
                return 0
            pos += 1
            if pos >= length:
                return 0
        if leading and s[pos] not in numSet:
            return 0
        if s[pos] == '-':
            sign = -1
            pos += 1
        elif s[pos] == '+':
            pos += 1
        if s[pos] not in numSet:
            return 0
        while s[pos] == '0':
            pos += 1
        intEnd = pos
        while intEnd < length:
            if s[intEnd] in numSet:
                intEnd += 1
                if intEnd - pos > 9:
                    sInt = int(s[pos:intEnd])
                    if sInt >= (2**31 - 1):
                        if sign > 0:
                            return (2**31) - 1
                        elif sInt >= (2**31):
                            return -(2**31)
            else:
                break
        if intEnd - pos < 1:
            return 0
        return sign * int(s[pos:intEnd])