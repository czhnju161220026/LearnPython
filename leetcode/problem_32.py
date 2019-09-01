# encoding=utf-8
'''
给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。
示例 1:

输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"
示例 2:

输入: ")()())"
输出: 4
解释: 最长有效括号子串为 "()()"
'''


class Solution:
    # 动态规划复杂度太高
    # 对于括号匹配问题应该优先考虑使用栈进行判断
    def longestValidParentheses_dp(self, s: str) -> int:
        length = len(s)
        # print(length)
        valid = [[i == j for i in range(length)] for j in range(length)]
        for begin in range(length - 1):
            if s[begin:begin + 2] == '()':
                valid[begin][begin + 1] = True
        # print(valid)
        longest = 0
        for step in range(2, length + 2, 2):
            for begin in range(length - step + 1):
                end = begin + step - 1
                for split_point in range(begin, end + 1, 2):
                    if valid[begin][split_point - 1] and valid[split_point][end]:
                        valid[begin][end] = True
                if valid[begin][end]:
                    if step > longest:
                        longest = step
                        # print('[%r,%r] is longest: %r' % (begin, end, step))
                elif s[begin] == '(' and s[end] == ')' and valid[begin + 1][end - 1]:
                    valid[begin][end] = True
                    if step > longest:
                        longest = step
                        # print('[%r,%r] is longest: %r' % (begin, end, step))
        return longest

    def longestValidParentheses(self, s: str) -> int:
        stack = []
        longest = 0
        temp = 0
        valid = True
        for c in s:
            if c == ')' and len(stack) == 0:
                valid = False
                if temp > longest:
                    longest = temp
                    temp = 0
            elif valid:
                if c == '(':
                    stack.append('(')
                else:
                    stack.remove(stack[-1])
                    temp += 2
            else:
                if c == '(':
                    stack.append('(')
                    temp = 0
                    valid = True

        if temp > longest:
            longest = temp
        return longest


if __name__ == '__main__':
    print(Solution().longestValidParentheses(")((())(())))("))
