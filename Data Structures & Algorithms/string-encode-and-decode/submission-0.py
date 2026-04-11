class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded = []

        for s in strs:
            prefix = f"{len(s):04}"
            encoded.append(prefix + s)

        return "".join(encoded)

    def decode(self, s: str) -> List[str]:

        decoded = []
        index = 0
        total_length = len(s)
        
        while index < total_length:

            s_length = int(s[index:index + 4])
            index += 4

            word = s[index:index + s_length]
            decoded.append(word)
            index += s_length

        return decoded




