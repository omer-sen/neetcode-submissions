class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        currBest = 0
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
            if freq[i] > freq.get(currBest, 0):
                currBest = i
        return currBest
        