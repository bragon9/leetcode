from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        sorted_substr_dict = defaultdict(list)
        for substr in strs:
            sorted_substr = sorted(list(substr))
            sorted_substr_dict[tuple(sorted_substr)].append(substr)
        return sorted_substr_dict.values()
