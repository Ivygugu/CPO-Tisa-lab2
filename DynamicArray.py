import ctypes
import copy


class DynamicArray(object):
    def __init__(self, capacity=10, grow_factor=2) -> None:
        self._grow_factor = grow_factor
        self._size = 0
        self._capacity = capacity
        self._start = 0
        self._array = [None] * self._capacity

    def __len__(self) -> int:
        return self._size

    def __str__(self) -> str:
        return str(self._array[:self._size])

    def __iter__(self) -> 'DynamicArray':
        array = from_list(to_list(self))
        return array

    def __next__(self) -> int:
        if self._start <= self._size - 1:
            res = self._array[self._start]
            self._start += 1
            return res
        else:
            raise StopIteration

    def __eq__(self, other) -> bool:
        if not isinstance(other, DynamicArray):
            return False
        if self._capacity != other._capacity:
            return False
        if self._grow_factor != other._grow_factor:
            return False
        if self._size == other._size:
            flag = True
            for i in range(self._size):
                if self._array[i] != other._array[i]:
                    flag = False
                    break
            return flag
        return False

    def _make_array(self, c) -> 'DynamicArray':
        return (c * ctypes.py_object)()

    def _add(self, value) -> None:
        if self._size == self._capacity:
            self._resize(self._grow_factor * self._capacity)
        self._array[self._size] = value
        self._size += 1

    def _resize(self, c) -> None:
        B = self._make_array(c)
        for k in range(self._size):
            B[k] = self._array[k]
        self._array = B
        self._capacity = c


def cons(array, value) -> 'DynamicArray':
    if type(array) is not DynamicArray:
        new_array = DynamicArray()
        return cons(new_array, value)
    res = copy.deepcopy(array)
    res._add(value)
    return res


def length(self) -> int:
    if (self is None):
        return 0
    return self._size


def insert(self, index, value) -> 'DynamicArray':
    new_array = copy.deepcopy(self)

    if new_array._size == new_array._capacity:
        new_array._resize(new_array._growth_factor * new_array._capacity)
    for i in range(new_array._size - 1, index - 1, -1):
        new_array._array[i + 1] = new_array._array[i]
    new_array._array[index] = value
    new_array._size += 1
    return new_array


def to_list(array) -> list:
    if array is None:
        return []
    res = []
    for i in range(array._size):
        res.append(array._array[i])
    return res


def from_list(array) -> 'DynamicArray':
    res = DynamicArray()
    for i in array:
        res._add(i)
    return res


def find(array, f) -> bool:
    for i in array:
        if f(i):
            return True
    return False


def remove(array, idx) -> 'DynamicArray':
    if idx < 0 or idx >= array._size:
        raise Exception('the index is not in Dynamic array')
    new_array = copy.deepcopy(array)
    for i in range(new_array._size):
        if i == idx:
            for j in range(i, new_array._size - 1):
                new_array._array[j] = new_array._array[j + 1]
            new_array._array[new_array._size - 1] = None
            new_array._size -= 1
            return new_array
    raise AssertionError('value not found')


def member(array, value) -> bool:
    """ Gets array elements based on index """
    for i in range(array._size):
        if (array._array[i] == value):
            return True
    return False


def filter(self, f) -> list:
    res = []
    for i in range(self._size):
        if (f(self._array[i])):
            res.append(self._array[i])
    return res


def map(self, f) -> 'DynamicArray':
    new_array = copy.deepcopy(self)
    for i in range(new_array._size):
        new_array._array[i] = f(new_array._array[i])
    return new_array


def reduce(self, f, initial_state) -> int:
    state = initial_state
    for i in range(self._size):
        state = f(state, self._array[i])
    return state


def empty(self) -> 'DynamicArray':
    return DynamicArray()


def reverse(array) -> 'DynamicArray':
    lst = to_list(array)
    lst.reverse()
    return from_list(lst)


def iterator(array) -> 'DynamicArray':
    return iter(array)


def concat(array1, array2) -> 'DynamicArray':
    res = DynamicArray()
    for i in range(array1._size):
        res._add(array1._array[i])
    for i in range(array2._size):
        res._add(array2._array[i])
    return res
