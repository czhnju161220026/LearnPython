# encoding=utf-8
'''
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例:

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。
'''


class Solution:
    def minPathSum(self, grid) -> int:
        height = len(grid)
        if height == 0:
            return 0
        width = len(grid[0])
        min_sum = [[0 for j in range(width)] for i in range(height)]
        min_sum[0][0] = grid[0][0]
        for i in range(height):
            for j in (range(width) if i != 0 else range(1, width)):
                if i == 0:
                    min_sum[i][j] = grid[i][j] + min_sum[i][j - 1]
                elif j == 0:
                    min_sum[i][j] = grid[i][j] + min_sum[i - 1][j]
                else:
                    min_sum[i][j] = grid[i][j] + min(min_sum[i - 1][j], min_sum[i][j - 1])
        return min_sum[height - 1][width - 1]


if __name__ == '__main__':
    grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]

    print(Solution().minPathSum(grid))
