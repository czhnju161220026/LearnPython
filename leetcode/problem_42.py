# encoding = utf-8
'''
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Marcos 贡献此图。

示例:
'''


class Solution:
    def trap(self, height: list) -> int:
        if len(height) == 0:
            return 0
        max_height = max(height)
        index = height.index(max_height)
        # print(index)
        res = 0
        if index > 1:
            current = height[0]
            for i in range(1, index):
                if height[i] < current:
                    res += (current - height[i])
                if current < height[i]:
                    current = height[i]
        # print(res)
        if index < len(height) - 2:
            current = height[-1]
            for i in range(len(height) - 2, index, -1):
                if height[i] < current:
                    res += (current - height[i])
                if current < height[i]:
                    current = height[i]
        return res


if __name__ == '__main__':
    print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
