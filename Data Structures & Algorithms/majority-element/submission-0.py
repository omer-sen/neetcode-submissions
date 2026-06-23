class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        currBest = 0
        for i in nums:
            freq[i] += 1
            if freq[i] > freq[currBest]:
                currBest = i
        return currBest
        