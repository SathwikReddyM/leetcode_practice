class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        x = set(nums)
        n = len(nums)//2
        for i in x:
            if nums.count(i) > n:
                return i
                break
        