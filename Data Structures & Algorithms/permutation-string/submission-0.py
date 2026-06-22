class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        l = 0
        state = dict()
        max_window = len(s1)
        dict1 = dict()
        
        # add s1 to a dict
        for ch in s1:
            dict1[ch] = dict1.get(ch, 0) + 1

        #######################################

        for r in range(len(s2)):
            
            while r - l + 1 > max_window:
                state[s2[l]] -= 1
                if state[s2[l]] == 0:
                    state.pop(s2[l])
                l += 1
            
            state[s2[r]] = state.get(s2[r], 0) + 1

            if state == dict1:
                return True


        return False