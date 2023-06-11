class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """for i in s:
            #print(i,t)
            if i in t:
                t = t.replace(i,"",1)
            else:
                return False
        return len(t) == 0"""
        if len(s) != len(t):
            return False
        for i in set(s):
            if s.count(i) != t.count(i):
                return False
        return True