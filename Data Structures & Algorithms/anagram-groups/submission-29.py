class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # sort the word and set as a key in a dict

        res = defaultdict(list)

        for word in strs:
            key = tuple(sorted(word))
            res[key].append(word)

        return list(res.values())