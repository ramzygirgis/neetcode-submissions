class Solution:
    def isPalindrome(self, s: str) -> bool:
        charlist = []
        for char in s:
            if char.isalnum():
                charlist.append(char.lower())
        reverse = []
        length = len(charlist)
        for i in range(length):
            reverse.append(charlist[length - i - 1])
        return charlist == reverse
            

        # s = ''.join(charlist)
        # appearances = {}
        # for i in range(length):
        #     appearances.setdefault(s[i], []).append(i)
        # for L in appearances.values():
        #     for i in L:
        #         if length - i - 1 not in L:
        #             return False
        # return True