class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        points = {}
        for n in nums:
            points[n-1] = n

        lengths = {}
        points_keys = points.keys()
        visited = []
        nums = set(nums)
        for n in nums:
            # print(f'checking number: {n}')
            # print(f'visitors: {visited}')
            lengths[n] = 1
            if (n in visited) or (n not in points_keys): # if n has no next element
                # print(f'{n} has no neighbour. continuing...')
                continue
            visited.append(n)
            next_up = points[n]
            visited.append(next_up)
            # print(f'next up: {next_up}')
            # print(f'visited: {visited}')
            exit = False
            while next_up in points_keys: # while there is a "next element"
                # print(f'length of current chain: {lengths[n]}')
                # print(f'next up ({next_up}) points to something')
                if next_up in lengths.keys(): # if next_up has been explored
                    lengths[n] += lengths[next_up] # connect the chains
                    # print(f'next up ({next_up}) has its own chain, of length {lengths[next_up]}')
                    # print(f'updated length of chain: {lengths[n]}')
                    next_up = 'not a key'
                    exit = True
                    continue
                else:
                    lengths[n] += 1
                    next_up = points[next_up]
            if exit:
                continue
            lengths[n] += 1 # tail, possible cause of bugs when there is a next element and we continue out of loop
            # print(f'last guy ({next_up}) has no next guy, so we added one.')
            #print(f'final length of chain: {lengths[n]}')
        max_so_far = 0
        for n in lengths.keys():
            #print(f'n: {n}, length of n: {lengths[n]}, max so far: {max_so_far}')
            if lengths[n] > max_so_far:
                max_so_far = lengths[n]
        return max_so_far
            
            
            
        
