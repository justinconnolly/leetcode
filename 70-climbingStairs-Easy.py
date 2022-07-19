class Solution:
    stairs_dict = {}
    def climbStairs(self, n: int) -> int:
        return self.climb_stairs(n)
    """
    subproblem: n - 1, n - 2
    base: n = 0, 1, 2
    """
    def climb_stairs(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n in self.stairs_dict:
            return self.stairs_dict[n]
        else:
            self.stairs_dict[n] = self.climb_stairs(n - 1) + self.climb_stairs(n - 2)
        return self.stairs_dict[n]