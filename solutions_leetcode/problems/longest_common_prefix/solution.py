class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        x = min(strs,key=len)
        for i in range(len(x)):
            for j in strs:
                if j[i] != x[i]:
                    return x[:i]
        return x