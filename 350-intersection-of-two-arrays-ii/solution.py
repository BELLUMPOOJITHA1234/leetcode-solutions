// 3 ms | 19.2 MB
class Solution:
    def intersect(self, nums1, nums2):
        count = {}
        ans = []

        for x in nums1:
            count[x] = count.get(x, 0) + 1

        for x in nums2:
            if count.get(x, 0) > 0:
                ans.append(x)
                count[x] -= 1

        return ans