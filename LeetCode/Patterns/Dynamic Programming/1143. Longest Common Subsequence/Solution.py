class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        def sub(i,j):
            if i<0 or j<0:
                return 0
            if s1[i]==s2[j]:
                return 1+ sub(i-1,j-1)
            return max(sub(i-1,j),sub(i,j-1))
        return sub(len(s1)-1,len(s2)-1)