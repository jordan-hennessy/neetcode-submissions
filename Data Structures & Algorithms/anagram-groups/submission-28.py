class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # We could use the word sorted as a key in a dict
        # Have to `append` since it is a list
        # Could use default dict (can't remember fully)
        
        res = dict()

        for word in strs:
            key = tuple(sorted(word))
            res[key] = res.get(key, [])
            res[key].append(word)
        
        return list(res.values())
            

