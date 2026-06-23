class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        retList = []
        for i in nums:
            count[i] = count.get(i, 0) + 1
        for n, c in count.items():
            freq[c].append(n)
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                retList.append(n)
                if len(retList) == k:
                    return retList

        
        