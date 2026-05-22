class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        for i in range(len(heights)):
            l = i
            r = i
            while l >= 0 and heights[i] <= heights[l]:
                l -= 1
            l += 1
            while r < len(heights) and heights[i] <= heights[r]:
                r += 1
            r -= 1
            area = (r - l + 1) * heights[i]
            print(area)
            res = max(res, area)
        return res
