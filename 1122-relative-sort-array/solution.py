// 0 ms | 19.2 MB
class Solution:
    def relativeSortArray(self, arr1, arr2):
        count = {}

        for x in arr1:
            count[x] = count.get(x, 0) + 1

        ans = []

        for x in arr2:
            if x in count:
                ans += [x] * count[x]
                del count[x]

        remaining = []

        for x in count:
            remaining += [x] * count[x]

        remaining.sort()

        return ans + remaining