class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        Neg = 1
        if x < 0:
            Neg = -1
            x = x * -1
        x = str(x)[::-1]
        if int(x) >= ((2**31)-1):
            return 0
        else:
            return int(x)*Neg
