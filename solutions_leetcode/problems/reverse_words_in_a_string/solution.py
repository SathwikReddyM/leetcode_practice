class Solution:
    def reverseWords(self, s: str) -> str:
        x = s.strip(" ").split(" ")
        x = [i for i in x if i != '']
        return " ".join(x[::-1])
        