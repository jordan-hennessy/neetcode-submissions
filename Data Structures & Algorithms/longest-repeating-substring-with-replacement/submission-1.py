class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        state = dict()
        # {"X": 2, "Y": 2}
        res = 0
        l = 0
        max_freq = 0

        for r in range(len(s)):
            state[s[r]] = state.get(s[r] , 0) + 1

            window_size = r - l + 1
            max_freq = max(max_freq, state[s[r]])

            while (window_size - max_freq) > k:
                state[s[l]] -= 1
                l += 1
                window_size -= 1
            
            res = max(res, r - l + 1)
        
        return res
