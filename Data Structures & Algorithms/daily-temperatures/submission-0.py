class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        length = len(temperatures)
        result = [0] * length
        for i in range(length):
            if len(stack) == 0 or temperatures[stack[-1]] >= temperatures[i]: # does warmer mean strictly warmer?
                stack.append(i)
            else:
                while len(stack) >= 1 and temperatures[stack[-1]] < temperatures[i]:
                    index = stack.pop()
                    result[index] = i - index
                stack.append(i)
        return result
                    