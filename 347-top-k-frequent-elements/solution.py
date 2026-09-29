// 5 ms | 22.7 MB
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}

        for x in nums:
            count[x] = count.get(x, 0) + 1

        arr = list(count.keys())
        arr.sort(key=lambda x: count[x], reverse=True)

        return arr[:k]