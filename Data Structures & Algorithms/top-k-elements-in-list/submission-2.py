class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_set = set(nums)
        frequency = {}
        for number in num_set:
            frequency[number] = 0
        for number in nums:
            frequency[number] += 1
        counts = frequency.values()
        inverse_frequency = {}
        for number in num_set:
            inverse_frequency[frequency[number]] = []
        for number in num_set:
            inverse_frequency[frequency[number]].append(number)
        selected = []
        num_selected = 0
        keys = inverse_frequency.keys()
        for i in range(len(nums), 0, -1):
            if num_selected == k:
                break
            if i not in keys:
                continue
            for elt in inverse_frequency[i]: 
                selected.append(elt) #since unique, this works, as we don't surpass
                print(elt)    
            num_selected += len(inverse_frequency[i])
        return selected
            