class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 0:
            return 0
        maxSoFar = 0
        chars = set(list(s))
        for C in chars:
            l = 0
            r = 0
            num_appearances = 0
            while l < len(s): # l is where we start. we look for the start of each block
                if s[l] != C:
                    l += 1
                    continue
                if s[l] == C:
                    num_appearances += 1
                    if l != 0 and s[l - 1] == C:
                        l +=1
                        continue
                    # now we at the start of a block.
                    count = 0
                    r = l
                    while r < len(s) and count <= r:
                        if s[r] == C:
                            r += 1
                        else:
                            if count == k:
                                break # no more flips allowed, we have reached the end
                            count += 1
                            r += 1
                    if num_appearances == 1:
                        while l >= 0 and count <= k:
                            if s[l] == C:
                                if l == 0:
                                    break
                                l -= 1
                                continue
                            if count == k:
                                l += 1
                                break
                            count += 1
                            if l == 0:
                                break
                            l -= 1
                        print(f'C: {C}, l: {l}, r:{r}')
                        
                        # while l >= 0 and count <= k:
                        #     if s[l] == C:
                        #         l -= 1
                        #     else:
                        #         if count == k:
                        #             l -=1
                        #             break # no more flips allowed, we have reached the end
                        #         count += 1
                        #         l -= 1
                        # print(f'char: {C}, l: {l}, r: {r}')
                        # l += 1
                    maxSoFar = max(maxSoFar, r - l)
                    if r == len(s):
                        break # this is the most we'll squeeze out of C
                    l += 1
        return maxSoFar
                            