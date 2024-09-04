from typing import List
from collections import defaultdict

class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            encoded.append(str(len(s)) + "," + s)
        return "".join(encoded)

    # def wrong_decode(self, s: str) -> List[str]:
    #     decoded = []
    #     length = ""
    #     for idx, letter in enumerate(s):
    #         if letter.isdigit():
    #             if s[idx+1] == "_":
    #                 length = int(length + letter)
    #                 decoded += [s[idx+2:idx+2+length]]
    #                 length = ""
    #             else:
    #                 length += letter
    #     return decoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            comma_idx = i
            while s[j] != ",":
                 comma_idx += 1
            length = int(s[i:comma_idx])
            decoded.append(s[comma_idx+1:comma_idx+1+length])
            i = comma_idx + 1 + length
        return decoded
        
print(Solution().decode(Solution().encode(["strenuously"])))
print(Solution().decode(Solution().encode(["1,23","45,6","7,8,9"])))
print(Solution().decode("10,234234,1,24,45,65,7,8,9"))
