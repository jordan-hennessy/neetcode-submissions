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
                word_len = int(s[index: index + 4])
                index += 4

                word = s[index : index + word_len]
                decoded.append(word)
                index += word_len

            return decoded