# encoding=utf-8
'''
给定一个化学式formula（作为字符串），返回每种原子的数量。

原子总是以一个大写字母开始，接着跟随0个或任意个小写字母，表示原子的名字。

如果数量大于 1，原子后会跟着数字表示原子的数量。如果数量等于 1 则不会跟数字。例如，H2O 和 H2O2 是可行的，但 H1O2 这个表达是不可行的。

两个化学式连在一起是新的化学式。例如 H2O2He3Mg4 也是化学式。

一个括号中的化学式和数字（可选择性添加）也是化学式。例如 (H2O2) 和 (H2O2)3 是化学式。

给定一个化学式，输出所有原子的数量。格式为：第一个（按字典序）原子的名子，跟着它的数量（如果数量大于 1），然后是第二个原子的名字（按字典序），跟着它的数量（如果数量大于 1），以此类推。

示例 1:

输入:
formula = "H2O"
输出: "H2O"
解释:
原子的数量是 {'H': 2, 'O': 1}。
'''


class Solution:
    @staticmethod
    def nextNum(formula: str, begin: int):
        if begin >= len(formula) or not formula[begin].isdecimal():
            return 1, begin
        else:
            num = ''
            while begin < len(formula) and formula[begin].isdecimal():
                num += formula[begin]
                begin += 1
            return int(num), begin


    @staticmethod
    def nextSubFormula(formula: str, begin: int):
        left_count = 1
        begin += 1
        sub_formula = ''
        while left_count != 0:
            if formula[begin] == ')':
                left_count -= 1
                if left_count != 0:
                    sub_formula += ')'
            elif formula[begin] == '(':
                left_count += 1
                sub_formula += '('
            else:
                sub_formula += formula[begin]
            begin += 1
        return sub_formula, begin

    @staticmethod
    def nextAtom(formula: str, begin: int):
        atom = formula[begin]
        begin += 1
        if begin >= len(formula):
            return atom, begin
        while begin < len(formula) and formula[begin].islower():
            atom += formula[begin]
            begin += 1
        return atom, begin

    def analyze(self, formula: str) -> dict:
        i = 0
        atoms = {}
        while i < len(formula):
            if formula[i].isupper():
                atom, i = Solution.nextAtom(formula, i)
                num, i = Solution.nextNum(formula, i)
                if atom not in atoms:
                    atoms[atom] = num
                else:
                    atoms[atom] += num
            elif formula[i] == '(':
                sub_formula, i = Solution.nextSubFormula(formula, i)
                num, i = Solution.nextNum(formula, i)
                sub_atoms = self.analyze(sub_formula)
                for sub_atom in sub_atoms:
                    if sub_atom not in atoms:
                        atoms[sub_atom] = num * sub_atoms[sub_atom]
                    else:
                        atoms[sub_atom] += num * sub_atoms[sub_atom]
        return atoms

    def countOfAtoms(self, formula: str) -> str:
        atoms = self.analyze(formula)
        res = ''
        for atom in sorted(atoms.keys()):
            res += atom
            res += '' if atoms[atom] == 1 else str(atoms[atom])
        return res


if __name__ == '__main__':
    print(Solution().countOfAtoms("K4(ON(SO3)2)2"))
