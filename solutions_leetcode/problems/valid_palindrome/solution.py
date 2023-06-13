class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans = ""
        for i in s:
            if (ord(i) >= 48 and ord(i) <= 57) or (ord(i) >= 65 and ord(i) <= 90) or (ord(i) >= 97 and ord(i) <= 122):
                ans += i
        #ans = ans.lower()
        #for j in range(int(len(ans)/2)):
         #   if ans[j] != ans[len(ans)-j-1]:
          #      return False
        return ans[:].lower() == ans[::-1].lower()
        """if len(s) < 2:
            return True
        i = 0
        j = len(s) - 1
        while i < j:
            #print(i,j)
            if not ((ord(s[i]) >= 48 and ord(s[i]) <= 57) or (ord(s[i]) >= 65 and ord(s[i]) <= 90) or (ord(s[i]) >= 97 and ord(s[i]) <= 122)):
                i+=1
                continue
            elif not ((ord(s[j]) >= 48 and ord(s[j]) <= 57) or (ord(s[j]) >= 65 and ord(s[j]) <= 90) or (ord(s[j]) >= 97 and ord(s[j]) <= 122)):
                j-=1
                continue
            else:
                if s[i].lower() != s[j].lower():
                    return False
                i+=1
                j-=1
        return True"""