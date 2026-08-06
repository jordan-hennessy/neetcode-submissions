class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        state = set()
        left = 0
        res = 0

        for right in range(len(s)):

            while s[right] in state:
                state.remove(s[left])
                left += 1
            res = max(res, right - left + 1)
            state.add(s[right])
        
        return res