class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        lis = nums
        lis.extend(nums)
        return lis