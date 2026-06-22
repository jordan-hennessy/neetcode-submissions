class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        state = set()
        res = 0

        for r in range(len(s)):
            while s[r] in state:
                state.remove(s[l])
                l += 1
            state.add(s[r])

            res = max(res, r - l + 1)

        return res