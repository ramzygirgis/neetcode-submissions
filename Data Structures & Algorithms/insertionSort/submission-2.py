# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        states = []
        if len(pairs) == 0:
            return []
        for i in range(1, len(pairs)):
            states.append(pairs.copy())
            j = i - 1
            while j >= 0 and pairs[j].key > pairs[j + 1].key:
                placeholder = pairs[j]
                pairs[j] = pairs[j + 1]
                pairs[j + 1] = placeholder
                j -= 1
        states.append(pairs.copy())
        return states

            







        # states = []
        # for i in range(len(pairs)):
        #     min_index = i
        #     for j in range(i + 1, len(pairs)):
        #         if pairs[j].key < pairs[min_index].key:
        #             min_index = j
        #     placeholder = pairs[i]
        #     pairs[i] = pairs[min_index]
        #     pairs[min_index] = placeholder
        #     states.append(list(pairs))
        # return states