class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ''
        for s in strs:
            encoded_string += f'{len(s)}:{s}'
        return encoded_string
    def decode(self, s: str) -> List[str]:
        length = len(s)
        i = 0
        strs = []
        while i < len(s):
            num = ''
            while s[i] != ':':
                num += s[i]
                i += 1
            i += 1
            cur_string = ''
            num = int(num)
            for _ in range(num):
                cur_string += s[i]
                i += 1
            strs.append(cur_string)
        return strs
