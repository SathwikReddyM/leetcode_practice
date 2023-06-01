class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        box = {}
        j = 0
        for i in range(len(nums)):
            if nums[i] not in box:
                box[nums[i]] = 1
            else:
                box[nums[i]] += 1
            if box[nums[i]] < 3:
                nums[j] = nums[i]
                j+=1
        return j