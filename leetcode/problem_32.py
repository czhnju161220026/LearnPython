# encoding=utf-8


''' 给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

示例 1:

输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"
示例 2:

输入: ")()())"
输出: 4
解释: 最长有效括号子串为 "()()" '''


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        longest = [0] * len(s)
        for i, c in enumerate(s):
            if c == '(':
                longest[i] = 0
            else:
                if i > 0 and s[i-1] == '(':
                    longest[i] = 2 + (0 if i == 1 else longest[i-2])
                elif i > 0 and s[i-1] == ')':
                    index = i - 1 - longest[i-1]
                    if index >= 0 and s[index] == '(':
                        longest[i] = 2 + longest[i-1] + (0 if index == 0 else longest[index-1])

        #print(longest)
        return  0 if len(longest) == 0 else max(longest)


if __name__ == '__main__':
    print(Solution().longestValidParentheses( "()(())"))
