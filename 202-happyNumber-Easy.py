class Solution:
    def isHappy(self, n: int) -> bool:
        def is_happy(n, n_set):
            if n == 1:
                return True
            if n in n_set:
                return False
            n_set.add(n)
            sum = 0
            while n > 0:
                unit = n % 10
                sum += unit ** 2
                n //= 10
            return is_happy(sum, n_set)
        happy_set = set()
        return is_happy(n, happy_set)