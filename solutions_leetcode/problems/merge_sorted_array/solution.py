class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        j = 0
        for i in nums2:
            while nums1[j] <= i and j < m:
                j+=1
            nums1.insert(j,i)
            nums1.pop(-1)
            m+=1
            print(nums1)