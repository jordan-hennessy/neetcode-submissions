class Solution:
    def minWindow(self, s: str, t: str) -> str:

        window = dict()
        left = 0
        res_left = 0
        res_right = 0
        res_len = 1001
        t_dict = dict()

        # make t a dict
        for ch in t:
            t_dict[ch] = t_dict.get(ch, 0) + 1

        # 'have' increases when we have all of a letter from t in window
        have = 0
        need = len(t_dict)

        #####################
        for right in range(len(s)):
            ch = s[right]

            # Check to see if ch is in t
            if ch in t:
                window[ch] = window.get(ch, 0) + 1
                if window[ch] == t_dict[ch]:
                    have += 1

            while have == need:
                if (right - left + 1) < res_len:
                    res_len = right - left + 1
                    res_right, res_left = right, left

                if s[left] in t_dict:
                    window[s[left]] -= 1
                    if window[s[left]] < t_dict[s[left]]:
                        have -= 1

                left += 1

        return s[res_left:res_right + 1] if res_len != 1001 else ""
