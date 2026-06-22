class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        offset = len(nums)
        newArr = [0] * (len(nums) * 2)
        for index, i in enumerate(nums):
            newArr[index] = i
            newArr[offset+index]=i
        return newArr