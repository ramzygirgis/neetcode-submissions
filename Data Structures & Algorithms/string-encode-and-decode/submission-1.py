class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ''
        for s in strs:
            encoded_str += str(len(s)) + '#' + s
        return encoded_str

    def decode(self, s: str) -> List[str]:
        length = len(s)
        i = 0
        strs = []
        while i < length:
            num = ''
            while s[i] != '#':
                num += s[i]
                i += 1
            i += 1
            num = int(num)
            cur_str = s[i: i + num]
            i += num
            strs.append(cur_str)
            print(i)
        return strs

