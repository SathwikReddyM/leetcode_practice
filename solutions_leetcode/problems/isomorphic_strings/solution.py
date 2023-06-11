class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        x = []
        for i in list(dict.fromkeys(s)):
            x.append(s.count(i))
        z = list(dict.fromkeys(t))
        for j in range(len(z)):
            if t.count(z[j]) != x[j]:
                return False
        a = {}
        for i in range(len(s)):
            if s[i] not in a:
                a[s[i]] = t[i]
            else:
                if a[s[i]] != t[i]:
                    return False
        return True
