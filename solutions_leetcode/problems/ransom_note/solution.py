class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """for i in range(len(ransomNote)):
            #print(ransomNote[i],magazine)
            if ransomNote[i] in magazine:
                magazine = magazine.replace(ransomNote[i],"",1)
            else:
                return False
        return True"""
        for i in set(ransomNote):
            if magazine.count(i) < ransomNote.count(i):
                return False
        return True