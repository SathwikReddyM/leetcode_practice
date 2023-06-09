class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """if len(haystack) == len(needle):
            if haystack == needle:
                return 0
            else:
                return -1
        else:"""
        """n = len(needle)
        for i in range(len(haystack)-n+1):
            print(haystack[i:i+n])
            if haystack[i:i+n] == needle:
                return i
                break
        return -1"""
        return haystack.find(needle)
