class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        x = []
        for i in range(numRows):
            x.append([])
        i = 1
        x[0].append(s[0])
        up =  True
        row = 1
        z = numRows - 1
        #print(x)
        while i < len(s):
            #print(i,row)
            #print(x)
            x[row].append(s[i])
            z-=1
            if z == 0:
                up = not up
                z = numRows -1
            if up:
                row+=1
            else:
                row -=1
            i+=1
        ans = ""
        for i in x:
            ans+="".join(i)
        return ans
        #first = row = 1, z = 3, up = t
        #first end = row = 2, z = 2, up = t
        #second = row = 3, z= 1, up = t
        #third = row = 2, z = 3, up = f
        #fourth = row = 1, z = 2, up = f
        #fifth = row = 0, z = 1, up = f
        #sixth = row = 1, z = 3, up = t