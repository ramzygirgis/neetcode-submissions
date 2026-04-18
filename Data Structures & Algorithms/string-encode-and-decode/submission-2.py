class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        words = []
        l = 0
        r = l
        while r < len(s):
            if s[r] == "#":
                num = int(s[l:r])
                word = s[r + 1: r + 1 + num]
                words.append(word)
                r += num
                l = r + 1
            r += 1
        return words
            
            
