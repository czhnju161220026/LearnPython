# encoding=utf-8
'''
给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

返回被除数 dividend 除以除数 divisor 得到的商。

示例 1:

输入: dividend = 10, divisor = 3
输出: 3
示例 2:

输入: dividend = 7, divisor = -3
输出: -2
说明:

被除数和除数均为 32 位有符号整数。
除数不为 0。
假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。本题中，如果除法结果溢出，则返回 231 − 1。
'''


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == 1:
            return dividend
        elif divisor == -1:
            return min(pow(2, 31) - 1, -dividend)
        else:
            result = 0
            if dividend < 0:
                dividend = -dividend
                divisor = -divisor
            step = 1 if divisor > 0 else -1
            while True:
                dividend -= (step * divisor)
                if dividend >= 0:
                    result += step
                    step *= 2
                else:
                    dividend += step * divisor
                    step /= 2
                if step == 0:
                    break
        return int(result)


if __name__ == '__main__':
    print(Solution().divide(-7, 2))
