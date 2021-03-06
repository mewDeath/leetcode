# -*- coding: utf-8 -*-
# @Author  : mew

from .solution import Solution
from .my_defs import *
import unittest
from pprint import pprint


class Template(unittest.TestCase):
    method = None

    def _assert_equal(self, inputs, outputs):
        if isinstance(inputs, tuple):
            return self.assertEqual(outputs, self.method(*inputs))
        return self.assertEqual(outputs, self.method(inputs))

    @unittest.skip
    def test_case(self):
        raise NotImplemented


class p10(Template):
    method = Solution.isMatch_p10

    def test_case(self):
        self._assert_equal(('aa', 'a*'), True)
        self._assert_equal(('ab', '.*'), True)
        self._assert_equal(('aab', 'c*a*b'), True)
        self._assert_equal(('mississippi', 'mis*is*p*.'), False)


class p18(Template):
    method = Solution.fourSum

    def test_case(self):
        inputs = ([-2, -1, -1, 1, 1, 2, 2], 0)
        outputs = [[-2, -1, 1, 2], [-1, -1, 1, 1]]
        self._assert_equal(inputs, outputs)


class p20(unittest.TestCase):
    method = Solution().isValid

    def test_case(self):
        s = "()[]{}"
        self.assertEqual(self.method(s), True)
        s = "("
        self.assertEqual(self.method(s), False)


class p21(unittest.TestCase):
    method = Solution().mergeTwoLists

    def test_case(self):
        l1 = myList([1, 2, 4])
        l2 = myList([1, 3, 4])
        res = myList([1, 1, 2, 3, 4, 4])
        for i, j in zip(myList(self.method(l1.first_node, l2.first_node)), res):
            self.assertEqual(i.val, j.val)


class p19(unittest.TestCase):
    method = Solution().removeNthFromEnd

    def _assert_equal(self, inputs, outputs):
        head, n = inputs
        res = outputs
        process = self.method(myList(head).first_node, n)
        self.assertEqual(myList(process).to_list(), res)

    def test_case(self):
        self._assert_equal(([1, 2, 3, 4, 5], 2), [1, 2, 3, 5])
        self._assert_equal(([1], 1), [])
        self._assert_equal(([1, 2], 1), [1])
        self._assert_equal(([1, 2], 2), [2])


class p34(unittest.TestCase):
    method = Solution().searchRange

    def _assert_equal(self, inputs, outputs):
        self.assertEqual(self.method(*inputs), outputs)

    def test_case(self):
        self._assert_equal(([5, 7, 7, 8, 8, 10], 8), [3, 4])
        self._assert_equal(([5, 7, 7, 8, 8, 10], 6), [-1, -1])
        self._assert_equal(([], 0), [-1, -1])


class p37(unittest.TestCase):
    method = Solution().solveSudoku

    def _assert_equal(self, inputs, outputs):
        self.method(inputs)
        self.assertEqual(inputs, outputs)

    def test_case(self):
        a = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
        b = [["5", "3", "4", "6", "7", "8", "9", "1", "2"],
             ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
             ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
             ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
             ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
             ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
             ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
             ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
             ["3", "4", "5", "2", "8", "6", "1", "7", "9"]]
        self._assert_equal(a, b)


class p39(unittest.TestCase):
    method = Solution().combinationSum

    def _assert_equal(self, inputs, outputs):
        res = self.method(*inputs)
        self.assertEqual(res, outputs)

    def test_case(self):
        self._assert_equal(([2, 3, 6, 7], 7),
                           [[2, 2, 3], [7]])


class p40(unittest.TestCase):
    method = Solution().combinationSum2

    def _assert_equal(self, inputs, outputs):
        res = self.method(*inputs)
        res.sort()
        outputs.sort()
        self.assertEqual(res, outputs)

    def test_case(self):
        self._assert_equal(([10, 1, 2, 7, 6, 1, 5], 8),
                           [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]])


class p41(unittest.TestCase):
    method = Solution().firstMissingPositive

    def _assert_equal(self, inputs, outputs):
        self.assertEqual(self.method(inputs), outputs)

    def test_case(self):
        self._assert_equal([3, 4, -1, 1], 2)
        self._assert_equal([], 1)
        self._assert_equal([1], 2)
        self._assert_equal([1, 1], 2)


class p84(Template):
    method = Solution().largestRectangleArea

    def test_case(self):
        self._assert_equal([2, 1, 5, 6, 2, 3], 10)


class p43(Template):
    method = Solution().multiply

    def test_case(self):
        self._assert_equal(('112', '1111'), '124432')


class p44(Template):
    method = Solution().isMatch

    def test_case(self):
        s = "babbbbaabababaabbababaababaabbaabababbaaababbababaaaaaabbabaaaabababbabbababbbaaaababbbabbbbbbbbbbaabbb"
        p = "b**bb**a**bba*b**a*bbb**aba***babbb*aa****aabb*bbb***a"
        self._assert_equal((s, p), False)
        self._assert_equal(('aabb', '*a*b'), True)


class p47(Template):
    method = Solution().permuteUnique

    def test_case(self):
        pprint(self.method([0, 0, 9, 0, 1]))


if __name__ == '__main__':
    p20().run()
    p21().run()
    p19().run()
