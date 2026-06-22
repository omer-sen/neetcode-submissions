class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}
        for index, i in enumerate(nums):
            targ = target - i
            
            if targ in numbers and numbers[targ] != index:
                return sorted([numbers[targ], index])
            numbers[i] = index