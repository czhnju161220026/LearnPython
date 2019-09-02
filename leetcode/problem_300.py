# encoding = utf-8

'''
给定一个无序的整数数组，找到其中最长上升子序列的长度。

示例:

输入: [10,9,2,5,3,7,101,18]
输出: 4
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
说明:

可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
你算法的时间复杂度应该为 O(n2) 。
进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?
'''


class Solution:
    def lengthOfLIS(self, nums: list) -> int:
        if len(nums) <= 1:
            return len(nums)
        length = [1] * len(nums)
        max_length = 0
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i] and length[j] + 1 > length[i]:
                    length[i] = length[j] + 1
            max_length = max(max_length, length[i])

        return max_length


if __name__ == '__main__':
    print(Solution().lengthOfLIS([10,9,2,5,3,7,101,18]))
