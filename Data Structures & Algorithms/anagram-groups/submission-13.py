class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = dict()

        for word in strs:
            key = tuple(sorted(word))
            res[key] = res.get(key, []) + [word]

        return list(res.values())