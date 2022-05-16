import unittest
from hypothesis import given
import hypothesis.strategies as st
from DynamicArray import cons, to_list, length, remove, member
from DynamicArray import empty, iterator, find, reverse
from DynamicArray import from_list, concat, filter, map, reduce, insert
from DynamicArray import DynamicArray


class DynamicArrayTest(unittest.TestCase):
    def test_api(self):

        empty = DynamicArray()
        l1 = cons(cons(empty, 1), None)
        l2 = cons(cons(empty, None), 1)
        # TODO: conj to add elements to the end
        self.assertEqual(str(empty), "[]")
        self.assertEqual(str(l1), "[1, None]")
        self.assertEqual(str(l2), "[None, 1]")
        self.assertNotEqual(empty, l1)
        self.assertNotEqual(empty, l2)
        self.assertNotEqual(l1, l2)
        self.assertEqual(l1, cons(cons(empty, 1), None))
        self.assertEqual(length(empty), 0)
        self.assertEqual(length(l1), 2)
        self.assertEqual(length(l2), 2)
        self.assertEqual(str(remove(l1, 0)), "[None]")
        self.assertEqual(str(remove(l1, 1)), "[1]")
        self.assertFalse(member(empty, None))
        self.assertTrue(member(l1, None))
        self.assertTrue(member(l1, 1))
        self.assertFalse(member(l1, 2))
        self.assertEqual(l1, reverse(l2))
        self.assertEqual(to_list(l1), [1, None])
        self.assertEqual(l1, from_list([1, None]))
        self.assertEqual(concat(l1, l2), from_list([1, None, None, 1]))

        buf = []
        for e in l1:
            buf.append(e)
        self.assertEqual(buf, [1, None])
        lst = to_list(l1) + to_list(l2)
        for e in l1:
            lst.remove(e)
        for e in l2:
            lst.remove(e)
        self.assertEqual(lst, [])

    def test_insert(self):
        x = [1, 2, 3]
        array = from_list(x)
        array2 = insert(array, 1, 4)
        self.assertEqual(to_list(array2), [1, 4, 2, 3])

    def test_find(self):
        x = [1, 2, 3, None]
        array = from_list(x)
        self.assertFalse(find(array, lambda x: x == 5))
        self.assertTrue(find(array, lambda x: x is None))
        self.assertTrue(find(array, lambda x: x % 2 == 0))

    def test_filter(self):
        x = [1, 2, 3, 4, 5]
        array = from_list(x)
        self.assertEqual([2, 4],  filter(array, lambda e: e % 2 == 0))

    def test_map(self):
        array = DynamicArray()
        self.assertEqual(to_list(map(array,str)), [])
        array = from_list([1, 2, 3])
        self.assertEqual(to_list(map(array, str)), ["1", "2", "3"])
        self.assertEqual(to_list(map(array, lambda x: x + 1)), [2, 3, 4])

    def test_reduce(self):
        array = DynamicArray()
        self.assertEqual(reduce(array, lambda st, e: st + e, 0), 0)

        # sum of list
        array = from_list([1, 2, 3])
        self.assertEqual(reduce(array, lambda st, e: st + e, 0), 6)
        # size
        test_data = [
            [],
            ['a'],
            ['a', 'b']
        ]
        for e in test_data:
            array = from_list(e)
            self.assertEqual(reduce(array, lambda st, _: st + 1, 0), l
                             ength(array))

    def test_empty(self):
        array = DynamicArray()
        a = empty(array)
        b = from_list([])
        self.assertEqual(a, b)

    def test_iter(self):
        x = [1, 2, 3]
        array = from_list(x)
        tmp = []
        try:
            it = iterator(array)
            while True:
                tmp.append(next(it))
        except StopIteration:
            pass
        self.assertEqual(x, tmp)
        self.assertEqual(to_list(array), tmp)
        it = iterator(DynamicArray())
        self.assertRaises(StopIteration, lambda: next(it))

    @given(st.lists(st.integers()))
    def test_from_list_to_list_equality(self, a):
        self.assertEqual(to_list(from_list(a)), a)

    @given(st.lists(st.integers()))
    def test_monoid_identity(self, lst):
        a = from_list(lst)
        empty = DynamicArray()
        self.assertEqual(concat(empty, a), a)
        self.assertEqual(concat(a, empty), a)

    @given(lst1=st.lists(st.integers()),
           lst2=st.lists(st.integers()),
           lst3=st.lists(st.integers()))
    def test_monoid_associativity(self, lst1, lst2, lst3):
        a = from_list(lst1)
        b = from_list(lst2)
        c = from_list(lst3)

        # mconcat: (a•b)•c = a•(b•c)
        self.assertEqual(concat(a, concat(b, c)),
                         concat(concat(a, b), c))

    if __name__ == '__main__':
        unittest.main()
