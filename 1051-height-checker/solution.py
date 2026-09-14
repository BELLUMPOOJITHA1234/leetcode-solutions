// 0 ms | 19.2 MB
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sor=sorted(heights)
        count=0
        for i in range(len(heights)):
            if heights[i]!=sor[i]:
                count+=1
        return count