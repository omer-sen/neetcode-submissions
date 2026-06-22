class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seen_a = {}
        
        for i in s:
            seen_a[i] = seen_a.get(i, 0) + 1
        for i in t:
            seen_a[i] = seen_a.get(i, 0) - 1
        for i in seen_a:
            if seen_a[i] != 0:
                return False
        return True
