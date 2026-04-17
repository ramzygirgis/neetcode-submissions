class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) == 0:
            return 0

        v = {}
        for i in range(len(position)):
            v[position[i]] = speed[i]
        position = sorted(position, reverse = True)
        stack = [0]

        for i in range(1, len(position)):

            if v[position[i]] == v[position[stack[-1]]]:
                stack.append(i)
                continue

            collision_x = (position[stack[-1]] * v[position[i]] - position[i] * v[position[stack[-1]]])/(v[position[i]] - v[position[stack[-1]]])
            if collision_x > target or collision_x < position[i]:
                stack.append(i)
                print(f'collision_x: {collision_x}, positioni: {position[i]}, stack[-1]: {stack[-1]}')
            # else:
            #     stack.pop()
            #     stack.append(i)
            
        return len(stack)