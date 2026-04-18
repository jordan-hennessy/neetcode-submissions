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
            s_len = int(s[index : index + 4])
            index += 4

            decoded.append(s[index : index + s_len])
            index += s_len

        return decoded