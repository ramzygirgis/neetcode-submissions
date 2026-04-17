class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {')': '(', ']': '[', '}': '{'}
        openers = matching.values()
        for c in s:
            if c in openers:
                stack.append(c)
            elif len(stack) == 0 or stack[len(stack) - 1] != matching[c]:
                return False
            else:
                stack.pop(len(stack) - 1)
        return len(stack) == 0