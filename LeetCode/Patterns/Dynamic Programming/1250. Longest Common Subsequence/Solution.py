class Solution:

    def longestCommonSubsequence(self, s1: str, s2: str) -> int:

        dp = [[-1] * len(s2) for _ in range(len(s1))]

        def sub(i, j):

            if i < 0 or j < 0:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            if s1[i] == s2[j]:
                dp[i][j] = 1 + sub(i - 1, j - 1)
            else:
                dp[i][j] = max(sub(i - 1, j), sub(i, j - 1))

            return dp[i][j]

        return sub(len(s1) - 1, len(s2) - 1)