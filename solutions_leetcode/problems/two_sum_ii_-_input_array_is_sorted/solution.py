class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """for i in range(len(numbers)-1,0,-1):
            if (target - numbers[i] in numbers):
                if numbers.index(target - numbers[i]) != i:
                    return [numbers.index(target-numbers[i])+1,i+1]"""
        """i = 0
        j = 1
        while i < len(numbers):
            while j < len(numbers):
                if numbers[i] + numbers[j] == target:
                    return [i+1,j+1]
                    break
                j+=1
            i+=1
            j = i+1"""
        i = 0
        j = len(numbers)-1
        while True:
            if numbers[i] + numbers[j] > target:
                j-=1
            elif numbers[i] + numbers[j] < target:
                i+=1
            else:
                return [i+1,j+1]
                