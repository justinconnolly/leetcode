class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == 0:
            return None
        if dividend == 0:
            return 0

        maxInt = (1 << 31) - 1
        minInt = 0 - (1 << 31)
        negative = False
        quotient = 0
        
        if dividend < 0:
            negative = not negative
            dividend = 0 - dividend
        if divisor < 0:
            negative = not negative
            divisor = 0 - divisor
        
        for i in range(31, -1, -1):
            if (divisor << i) <= dividend:
                dividend -= (divisor << i)
                quotient += 1 << i
        if negative:
            quotient = 0 - quotient
        if quotient < minInt:
            return minInt
        if quotient > maxInt:
            return maxInt
        return quotient 