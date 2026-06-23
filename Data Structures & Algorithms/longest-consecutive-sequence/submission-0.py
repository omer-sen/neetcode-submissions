class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        curr = 1
        currMax = 0
        
        for num in seen:
            if num-1 not in seen:
                curr = 1
                next_num = num+1
                while next_num in seen:
                    curr +=1
                    next_num +=1
                currMax = max(currMax, curr)
        return currMax
            