class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        x = {}
        y = {}
        s = s.split(" ")
        if len(s) != len(pattern):
            return False
        for i in range(len(s)):
            if s[i] not in x:
                x[s[i]] = pattern[i]
            if pattern[i] not in y:
                y[pattern[i]] = s[i]
        print(x,y)
        for i in range(len(s)):
            if x[s[i]] != pattern[i] or y[pattern[i]] != s[i]:
                return False
        return True

