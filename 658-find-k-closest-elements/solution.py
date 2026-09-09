// 0 ms | 20.6 MB
class Solution:
    def findClosestElements(self, arr, k, x):
        left = 0
        right = len(arr) - k

        while left < right:
            mid = (left + right) // 2

            if x - arr[mid] <= arr[mid + k] - x:
                right = mid
            else:
                left = mid + 1

        return arr[left:left + k]