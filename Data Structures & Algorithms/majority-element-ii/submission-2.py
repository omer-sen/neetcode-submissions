class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
        
        ret = []
        for n, c in freq.items():
            if c > len(nums)//3:
                ret.append(n)
        return ret