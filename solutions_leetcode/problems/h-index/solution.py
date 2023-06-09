class Solution:
    def hIndex(self, citations: List[int]) -> int:
        #x = sorted(set(citations),reverse = True)
        #print(x)
        ans = 0
        for i in range(max(citations),0,-1):
            #print(i)
            cnt = 0
            for j in citations:
                if j >= i:
                    cnt +=1
            #print(cnt)
            if cnt >= i:
                ans = i
                break
        return ans
