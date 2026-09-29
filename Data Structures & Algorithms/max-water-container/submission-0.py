class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        n = len(heights) 
        right = n - 1 
        res = 0

        while left < right:
            diff = abs(right - left)
            ht = min(heights[left], heights[right])
            a = diff * ht 
            res = max(res,a)

            if heights[left] > heights[right]: 
                right -= 1
            else:
                left+=1
        return res

        