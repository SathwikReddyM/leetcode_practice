class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """j = 0
        ans = 0
        box = []
        for i in range(len(nums)):
            if nums[i] not in box:
                box.append(nums[i])
                if i !=j:
                    nums[j] = nums[i]
                j+=1
            else:
                ans+=1
            #print(nums)
        return len(nums) - ans
        """
        count = {}
        j = 0
        for i in range(len(nums)):
            if nums[i] not in count:
                count[nums[i]] = 1
            else:
                count[nums[i]] += 1
        for i in range(len(nums)):
            if count[nums[i]] == 1:
                nums[j] = nums[i]
                j+=1
            else:
                count[nums[i]] -=1
        return j
            