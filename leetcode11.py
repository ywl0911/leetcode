# 解题思路：两个指针，分别从前往后和从后往前遍历，哪个指针对应的高度小，就移动哪个指针
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        max_area = 0
        while left < right:
            max_area = max((right - left) * min(height[left], height[right]), max_area)

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return max_area

# a = Solution()
# print(a.maxArea([1, 2, 3, 4]))
