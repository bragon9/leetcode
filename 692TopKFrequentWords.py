from collections import defaultdict
from bisect import bisect

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dict_count = defaultdict(int)
        for word in words:
            dict_count[word] += 1
        ans = []
        for word, count in dict_count.items():
            i = bisect(ans, (-count, word))
            if i < k:
                ans.insert(i, (-count, word))
            ans = ans[:k]
        return [i[1] for i in ans]
        
