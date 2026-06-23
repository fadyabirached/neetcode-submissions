class Solution:
    def maxArea(self, heights: List[int]) -> int:
        finalResult = 0

        left = 0 
        right = len(heights)-1

        while (left < right):
            result = (right-left)* min(heights[left],heights[right])

            if heights[left] < heights[right]:
                left = left+1
            else:
                right = right-1
            
            finalResult = max(finalResult, result)

        return finalResult

