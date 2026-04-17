class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict2 = {}
        for string in strs:
            sorted_string = sorted(string)
            sorted_string = ''.join(sorted_string)
            if sorted_string not in dict2.keys():
                dict2[sorted_string] = [string]
            else:
                dict2[sorted_string].append(string)
        L = [dict2[sorted_string] for sorted_string in dict2.keys()]     
        return L