import unittest

from hypothesis import given,settings
import hypothesis.strategies as st

from Immutable import *


class TestImmutableList(unittest.TestCase):
    def test_size(self):
        self.assertEqual(size(cons('a', None)), 1)
        lst = ['a', 'b']
        self.assertEqual(size(cons(lst, None)), 2)

    def test_cons(self):
        lst=['a','b','c','d','a','b','c']

        self.assertEqual(to_list(cons(['a','b','c','d','a','b','c'], None)),to_list(Node(['a','b','c','d','a','b','c'],None)))
        self.assertEqual(cons('a', cons('b', None)).elements, Node('a', Node('b', None)).elements)

    def test_remove(self):
        lst = ['a', 'b']
        self.assertEqual(to_list(remove(cons(lst, None), 'b')), to_list(cons('a', None)))
        lst = ['a', 'b', 'c']
        self.assertEqual(to_list(remove(cons(lst, None), 'b')), to_list(cons(['a', 'c'], None)))

    def test_to_list(self):
        self.assertEqual(to_list(None), [])
        self.assertEqual(to_list(cons('a', None)), ['a'])
        self.assertEqual(to_list(cons('a', cons('b', None))), ['a', 'b'])

    def test_from_list(self):
        test_data = [
            [],
            ['a'],
            ['a', 'b']
        ]
        for e in test_data:
            a=to_list(from_list(e))
            self.assertEqual(a, e)

    def test_map(self):
        lst=from_list([])
        lst=map(lst,str)
        lst=to_list(lst)
        self.assertEqual(lst, [])
        lst1=from_list([1, 2, 3])
        lst1=map(lst1,str)
        lst1=to_list(lst1)
        self.assertEqual(lst1, ["1", "2", "3"])

    def test_reduce(self):
        # sum of empty list
        lst=Node([],None)
        lst=reduce(lst,lambda st, e: st + e, 0)
        self.assertEqual(lst, 0)

        # sum of list
        lst=from_list([1, 2, 3])
        lst=reduce(lst,lambda st, e: st + e, 0)
        self.assertEqual(lst, 6)
        # size
        test_data = [
            ['a'],
            ['a','b'],
            ['a', 'b','c']
        ]
        for e in test_data:
            lst1=from_list(e)
            lst=reduce(lst1,lambda st, _: st + 1, 0)
            self.assertEqual(lst, lst1.size)

    def test_filter(self):
        def f(x):
            res = x + 1
            return res

        x = [1, 2, 3]
        lst=from_list(x)
        lst=filter(lst,f)
        self.assertEqual([2, 3, 4], to_list(lst))

    @given(st.lists(st.integers()))
    def test_from_list_to_list_equality(self, a):
        b=from_list(a)
        c=to_list(b)
        self.assertEqual(c, a)

    def test_iter(self):
        x=[1,2,3]
        lst=from_list(x)
        tmp=iterator(lst)
        self.assertEqual(x,tmp)

        # get_next=iterator([])
        # self.assertRaises(StopIteration,lambda :get_next())


if __name__ == '__main__':
    unittest.main()
