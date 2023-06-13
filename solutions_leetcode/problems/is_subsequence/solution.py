class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(t)<len(s):
            return False
        elif len(s)==0:
            return True
        j = 0
        while j < len(t) and len(s) > 0:
            if s[0] == t[j]:
                s = s[1:]
                j+=1
            else:
                j+=1
        return len(s) == 0
