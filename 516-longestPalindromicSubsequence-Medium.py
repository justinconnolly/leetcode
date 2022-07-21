class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        return self.L_dp(s, 0, len(s) - 1, dp = {})
    
    def L_dp(self,x, i, j, dp):
        if f"{i}-{j}" in dp:
            return dp[f"{i}-{j}"]
        if i == j:
                return 1
        if i > j:
            return 0
        if x[i] == x[j]:
            if i + 1 == j:
                return 2
            else:
                return 2 + self.L_dp(x, i + 1, j - 1, dp)
        else:
            dp[f"{i}-{j}"] = max(self.L_dp(x, i + 1, j, dp),
                                self.L_dp(x, i, j - 1, dp))
            return dp[f"{i}-{j}"]