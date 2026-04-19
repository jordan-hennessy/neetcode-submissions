class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded = []

        for word in strs:
            prefix = f"{len(word):04}"
            encoded.append(prefix + word)

        return "".join(encoded)

    def decode(self, s: str) -> List[str]:

        decoded = []
        index = 0

        while index < len(s):
            wLen = int(s[index : index + 4])
            index += 4

            decoded.append(s[index : index + wLen])
            index += wLen
        
        return decoded