class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0
        ans = 0
        for i in range(len(nums)):
            if nums[i] != val:
                if i !=j:
                    nums[j] = nums[i]
                j+=1
            else:
                ans+=1
            #print(nums)
        return len(nums) - ans


