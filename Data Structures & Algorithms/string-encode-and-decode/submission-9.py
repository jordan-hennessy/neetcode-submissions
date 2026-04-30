class Solution:

    def encode(self, strs: List[str]) -> str:

        encode = []

        for word in strs:
            prefix = f"{len(word):04}"
            encode.append(prefix + word)
        
        return "".join(encode)

    def decode(self, s: str) -> List[str]:

        decoded = []
        index = 0

        while index < len(s):
            wLen = int(s[index : index + 4])
            index += 4

            word = s[index : index + wLen]
            decoded.append(word)
            index += wLen

        return decoded