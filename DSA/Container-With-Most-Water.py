class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        s, e = 0, len(height) - 1
        max_area = 0

        while s < e:
            width = e - s
            area = min(height[s], height[e]) * width
            max_area = max(max_area, area)
            
            if height[s] < height[e]:
                s += 1
            else:
                e -= 1

        return max_area
        
                        


