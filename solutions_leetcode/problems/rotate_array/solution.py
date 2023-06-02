class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        nums = nums[-k:] + nums[:len(nums)-k]
        print(nums)
        
        for i in range(k):
            nums.insert(0,nums[-1])
            nums.pop(-1)"""
        k = k % len(nums)
        temp=nums[-k:]
        
        nums[k:]=nums[:-k]
    
        nums[:k]=temp 
        
        