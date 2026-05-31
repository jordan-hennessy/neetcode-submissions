class Solution:

    def encode(self, strs: List[str]) -> str:

        encode = []

        for word in strs:
            prefix = f"{len(word):04}"
            encode.append(prefix + word)
        
        return "".join(encode)

    def decode(self, s: str) -> List[str]:

        decode = []
        index = 0

        while index < len(s):
            wordLen = int(s[index : index + 4])
            index += 4

            word = s[index : index + wordLen]
            decode.append(word)
            index += wordLen
        
        return decode