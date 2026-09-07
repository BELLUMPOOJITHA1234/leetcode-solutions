// 7 ms | 20.2 MB
from collections import Counter

class Solution:
    def frequencySort(self, s):
        count = Counter(s)

        result = ""

        for ch, freq in count.most_common():
            result += ch * freq

        return result