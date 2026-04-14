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

        while index < len(s):
            sLen = int(s[index : index + 4])
            index += 4

            decoded.append(s[index : index + sLen])
            index += sLen
        
        return decoded
