class Solution:
    def isThree(self, n: int) -> bool:
        i = 1
        divisors = 1
        while i <= n//2:   
            if (n % i == 0) :
                divisors += 1
            i = i + 1
            if divisors > 3:
                return False
        if divisors == 3:
            return True
        return False

sol = Solution()
print(sol.isThree(9))